from beliefbase import BeliefBase
from agent import Agent

init_beliefs = [
    # atomic facts
    "TunnelCamerasOff",
    "AmbulanceDelay",
    "NoSeatbelt",
    "RoyalDisapproved",
    "PregnantWithDodi",
    "(RoyalDisapproved & PregnantWithDodi) >> MotiveForMurder",
    "MotiveForMurder >> MI6Involved",

    "MI6Involved >> TunnelCamerasOff",
    "MI6Involved >> AmbulanceDelay",
    "MI6Involved >> CarSabotaged",

    "(MI6Involved & CarSabotaged >> DianaKilled)",

    "(TunnelCamerasOff & AmbulanceDelay & NoSeatbelt) >> DianaKilled",

    "(PaparazziChase & NoSeatbelt) >> AccidentSeverityHigh",
    "(AccidentSeverityHigh & TunnelCamerasOff) >> Suspicious",
    "Suspicious >> DianaKilled",

    "PregnantWithDodi >> ThreatToMonarchy",
    "ThreatToMonarchy >> RoyalDisapproved",

    "RoyalDisapproved >> MI6Pressure",
    "MI6Pressure >> MI6Involved",


    "CoincidencesTooMany >> DianaKilled",
    # "(TunnelCamerasOff & AmbulanceDelay & CarSabotaged) >> CoincidencesTooMany",
]

agent = Agent(init_beliefs)
while not agent.quit:
    agent.ask_action()
