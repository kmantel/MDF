import psyneulink as pnl

Composition_0 = pnl.Composition(name="Composition-0")

input_layer = pnl.TransferMechanism(
    name="input_layer",
    function=pnl.Linear(default_variable=[[0.0, 0.0]]),
    termination_measure=pnl.Distance(
        metric=pnl.MAX_ABS_DIFF, default_variable=[[[0.0, 0.0]], [[0.0, 0.0]]]
    ),
    default_variable=[[0.0, 0.0]],
)
accumulator_layer = pnl.LCAMechanism(
    name="accumulator_layer",
    competition=0.2,
    function=pnl.Logistic(gain=2.0, default_variable=[[0.0, 0.0]]),
    hetero=-0.2,
    initial_value=[[0.0, 0.0]],
    integration_rate=0.2,
    noise=0.1,
    output_ports=["RESULTS"],
    termination_comparison_op=">=",
    termination_measure=pnl.TimeScale.TRIAL,
    termination_threshold=0.4,
    default_variable=[[0.0, 0.0]],
)

Composition_0.add_node(input_layer)
Composition_0.add_node(accumulator_layer)

Composition_0.add_projection(
    projection=pnl.MappingProjection(
        name="MappingProjection from input_layer[RESULT] to accumulator_layer[InputPort-0]",
        function=pnl.LinearMatrix(
            matrix=[[1.0, 0.0], [0.0, 1.0]], default_variable=[0.0, 0.0]
        ),
    ),
    sender=input_layer,
    receiver=accumulator_layer,
)


Composition_0.scheduler.termination_conds = {
    pnl.TimeScale.RUN: pnl.Never(),
    pnl.TimeScale.TRIAL: pnl.AllHaveRun(),
}
