file = open("output.txt", "wt")
file.write("The pistol shrimp, even though it might look weak, is a bang for your buck. These sharp-shooting crustaceans are far from quiet — their bubbles have measured in at 218 decibels, which is louder than a speeding bullet. To us humans the sound isn't actually that loud, but that's due to the blast only lasting a tiny fraction of a second.When the bubble pops, it generates heat that reaches 8,000 degrees Fahrenheit (4,427 degrees Celsius), four times hotter than lava. The heat dissipates at rapid speed so there are no lasting effects (except to the unfortunate small creature that felt its burn). Pistol shrimp are inspiring researchers in England as they work to replicate the process that heats up the sun, fusion power, to create an abundance of clean, safe energy — giving a big boost to the fight against climate change. Fusion power needs a high-velocity projectile to create a shockwave and collapse a plasma-filled cavity, and the pistol shrimp are the only creatures on Earth who naturally have such powers.")

file.close()

file = open("output.txt", "rt")
print(file.read)