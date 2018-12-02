"""Tools for naming and indexing simulated constructs."""


###############
### IMPORTS ###
###############


import typing as typ
import dataclasses 
import enum 


########################################
### BASE CLASS FOR CONSTRUCT SYMBOLS ###
########################################


@dataclasses.dataclass(init=True, repr=True, eq=False, frozen=True)
class ConstructSymbol(object):
    """
    General base class for symbols representing simulation constructs.
    
    Construct symbols are used to identify and carry essential information 
    about key simulated constructs in a lightweight manner. 
    
    In general, each construct symbol is associated with at least one construct 
    realizer, which defines the behavior of the model vis à vis that construct 
    in some particular context. For information on construct realizers see
    ``pyClarion.base.realizers``.
    """

    pass


##########################################
### BASIC CONSTRUCT SYMBOL DEFINITIONS ###
##########################################


@dataclasses.dataclass(init=True, repr=True, eq=False, frozen=True)
class BasicConstructSymbol(ConstructSymbol):
    """
    Base class for symbols for basic constructs.
    
    A construct is basic iff it may not contain other constructs.
    """

    pass


@dataclasses.dataclass(init=True, repr=True, eq=False, frozen=True)
class Node(BasicConstructSymbol):
    """Symbol for a generic connectionist node."""
    
    pass


@dataclasses.dataclass(init=True, repr=True, eq=True, frozen=True)
class Microfeature(Node):
    """
    Symbol for a microfeature node.

    Microfeature nodes represent implicit knowledge. They are characterized by 
    a dimension-value pair (dv-pair). Microfeatures that share the same 
    dimension entry are treated as mutual alternatives. 
    """

    dim: typ.Hashable
    val: typ.Hashable


@dataclasses.dataclass(init=True, repr=True, eq=True, frozen=True)
class Chunk(Node):
    """
    Symbol for a chunk node.
    
    Chunk nodes represent explicit knowledge. They are characterized by 
    an id.
    """

    id: typ.Hashable


class FlowType(enum.Flag):
    """
    Flag for signaling the direction(s) of an activation flow construct.

    Supports the ``Flow`` class.
    
    May take on four basic value:
        TT: Activation flows within the top-level.
        BB: Activation flows within the bottom-level.
        TB: Top-down activation flows.
        BT: Bottom-up activation flows.
    """

    TT = enum.auto()
    BB = enum.auto()
    TB = enum.auto()
    BT = enum.auto()


@dataclasses.dataclass(init=True, repr=True, eq=True, frozen=True)
class Flow(BasicConstructSymbol):
    """
    Symbol for an activation flow.
    
    A flow governs how the activation of some set of nodes may drive the 
    activation of another set of nodes.

    Flows are characterized by an id and a flow type. The flow type describes 
    what kinds of nodes are connected by a given flow. Typically, flows may 
    connect chunks to microfeatures (top-down), microfeatures to chunks 
    (bottom-up), chunks to chunks (top level) and microfeatures to 
    microfeatures (bottom level).
    """

    id: typ.Hashable
    flow_type: FlowType


@dataclasses.dataclass(init=True, repr=True, eq=True, frozen=True)
class Appraisal(BasicConstructSymbol):
    """Symbol for a class of judgments and/or decisions."""

    id: typ.Hashable


@dataclasses.dataclass(init=True, repr=True, eq=True, frozen=True)
class Behavior(BasicConstructSymbol):
    """Symbol for a collection of performable actions."""

    id: typ.Hashable


@dataclasses.dataclass(init=True, repr=True, eq=True, frozen=True)
class Buffer(BasicConstructSymbol):
    """Symbol for a temporary store of cognitive information."""

    id: typ.Hashable


##############################################
### CONTAINER CONSTRUCT SYMBOL DEFINITIONS ###
##############################################


@dataclasses.dataclass(init=True, repr=True, eq=False, frozen=True)
class ContainerConstructSymbol(ConstructSymbol):
    """
    Base class for symbols representing container constructs. 
    
    Container constructs may own other basic or container constructs.
    """

    pass


@dataclasses.dataclass(init=True, repr=True, eq=True, frozen=True)
class Subsystem(ContainerConstructSymbol):
    """Symbol for a cognitive subsystem.
    
    A cognitive subsystem is a large, functionally distinct section of a 
    complete cognitive apparatus.
    """

    id: typ.Hashable


@dataclasses.dataclass(init=True, repr=True, eq=True, frozen=True)
class Agent(ContainerConstructSymbol):
    """Symbol for an agent."""

    id: typ.Hashable
