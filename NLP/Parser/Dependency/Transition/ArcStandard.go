package Transition

import (
	. "chukuparser/Algorithm/Transition"
	. "chukuparser/NLP"
)

type ArcStandard struct {
	Relations []string
	oracle    *Oracle
}

// Verify that ArcStandard is a TransitionSystem
var _ TransitionSystem = &ArcStandard{}

func (a *ArcStandard) Transition(from *Configuration, transition Transition) *Configuration {
	conf := (*(*from).Copy()).(SimpleConfiguration)
	// Transition System:
	// LA-r	(S|wi,	wj|B,	A) => (S   ,	wj|B,	A+{(wj,r,wi)})	if: i != 0
	// RA-r	(S|wi, 	wj|B,	A) => (S   ,	wi|B, 	A+{(wi,r,wj)})
	// SH	(S   ,	wi|B, 	A) => (S|wi,	   B,	A)
	switch transition[:2] {
	case "LA":
		wi, _ := conf.Stack().Pop()
		if wi == 0 {
			panic("Attempted to LA the root")
		}
		wj, _ := conf.Queue().Peek()
		relation := (DepRel)(transition[3:])
		newArc := &BasicDepArc{wj, relation, wi}
		conf.Arcs().Add(newArc)
	case "RA":
		wi, _ := conf.Stack().Pop()
		wj, _ := conf.Queue().Pop()
		rel := (DepRel)(transition[3:])
		newArc := &BasicDepArc{wi, rel, wj}
		conf.Queue().Push(wi)
		conf.Arcs().Add(newArc)
	case "SH":
		wi, _ := conf.Queue().Pop()
		conf.Stack().Push(wi)
	}
	conf.SetLastTransition(transition)
	confAsInterface := (interface{})(conf)
	return confAsInterface.(*Configuration)
}

func (a *ArcStandard) TransitionTypes() []Transition {
	return []Transition{"LA-*", "RA-*", "SHIFT"}
}

func (a *ArcStandard) Projective() bool {
	return true
}

func (a *ArcStandard) Labeled() bool {
	return true
}

func (a *ArcStandard) Oracle() *Oracle {
	return a.oracle
}

func (a *ArcStandard) AddDefaultOracle() {
	if a.oracle == nil {
		oracle := (Oracle)(OracleFunction{})
		a.oracle = &oracle
	}
}

type OracleFunction struct {
	gold   *LabeledDependencyGraph
	arcSet *ArcSetSimple
}

var _ Decision = OracleFunction{}

func (o OracleFunction) SetGold(g *interface{}) {
	gold := (*g).(LabeledDependencyGraph)
	o.gold = &gold
	newArcSet := NewArcSetSimple(gold.NumberOfEdges())
	o.arcSet = &newArcSet
	for _, edgeNum := range gold.GetEdges() {
		arc := gold.GetLabeledArc(edgeNum)
		newArcSet.Add(*arc)
	}
}

func (o OracleFunction) GetTransition(conf *Configuration) Transition {
	c := (*conf).(SimpleConfiguration)

	if o.gold == nil {
		panic("Oracle needs gold reference, use SetGold")
	}
	// Given Gd=(Vd,Ad) # gold dependencies
	// o(c = (S,B,A)) =
	// LA-r	if	(B[0],r,S[0]) in Ad
	// RA-r	if	(S[0],r,B[0]) in Ad; and for all w,r', if (B[0],r',w) in Ad then (B[0],r',w) in A
	// SH	otherwise
	bTop, bExists := c.Queue().Peek()
	sTop, sExists := c.Stack().Peek()
	arcSet := *(o.arcSet)
	if bExists && sExists {
		// test if should Left-Attach
		arcs := arcSet.Get(BasicDepArc{bTop, "", sTop})
		if len(arcs) > 0 {
			arc := *(arcs[0])
			return (Transition)("LA-" + (string)(arc.GetRelation()))
		}

		// test if should Right-Attach
		arcs = arcSet.Get(BasicDepArc{sTop, "", bTop})
		if len(arcs) > 0 {
			reverseArcs := arcSet.Get(BasicDepArc{bTop, "", -1})
			// for all w,r', if (B[0],r',w) in Ad then (B[0],r',w) in A
			// otherwise, return SH
			for _, arc := range reverseArcs {
				revArcs := c.Arcs().Get(*arc)
				if len(revArcs) == 0 {
					return "SH"
				}
			}
			arc := *(arcs[0])
			return (Transition)("RA-" + (string)(arc.GetRelation()))
		}
	}
	return "SH"
}
