from simulator.runner.simulation_runner import SimulationRunner

runner = SimulationRunner(

    jobs=50,

    users=20,

    accounts=5,

)

runner.run()
