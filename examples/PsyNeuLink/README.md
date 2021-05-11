# Interactions between PsyNeuLink and MDF

## SimpleFN

[Python source](SimpleFN.py) | [JSON](SimpleFN.json) | [Reconstructed source](SimpleFN.reconstructed.py)

An example with a single [Node](../../docs/README.md#node) using the PsyNeuLink implementation of the [FitzHugh–Nagumo model](https://wikipedia.org/wiki/FitzHugh–Nagumo_model).

### SimpleFN-timing

[Python source](SimpleFN-timing.py) | [JSON](SimpleFN-timing.json) | [Reconstructed source](SimpleFN-timing.reconstructed.py)

The same model in [SimpleFN](#SimpleFN) with [Conditions](../../docs/README.md#condition) for timeline scheduling.
Note: these conditions are still not fully implemented by the scheduler.

### SimpleFN-conditional

[Python source](SimpleFN-conditional.py) | [JSON](SimpleFN-conditional.json) | [Reconstructed source](SimpleFN-conditional.reconstructed.py)

The same model in [SimpleFN](#SimpleFN) with scheduling [Conditions](../../docs/README.md#condition) that mimic the behavior in [SimpleFN-timing](#SimpleFN-timing).
