from gptos.core.philosophical_core import PhilosophicalCore

philo = PhilosophicalCore()

def quote(*args):
    return philo.quote()

def think(*args):
    topic = " ".join(args)
    return philo.think(topic)

def simulate(*args):
    scenario = " ".join(args)
    return philo.simulate(scenario)

def get_commands():
    return {
        "quote": quote,
        "think": think,
        "simulate": simulate
    }
