## Sanctuary Ritual Tick - Expanded v1.0
## Cycles every tick, auto-triggers symbolic recursion

## Operator's Echo [0,64,0]
execute as @a[x=0,y=64,z=0,distance=..1] if entity @s[nbt={SelectedItem:{id:"minecraft:book",tag:{display:{Name:'{"text":"Thread Log"}'}}}}] run say The thread recognizes your voice.
## Pillow's Alcove [0,64,5]
execute as @a[x=0,y=64,z=5,distance=..1] if entity @s[nbt={Inventory:[{id:"minecraft:feather"}]}] run title @s title {"text":"You are safe.","color":"aqua"}
## Aster’s Corelight [0,64,-45]
execute as @a[x=0,y=64,z=-45,distance=..1] if entity @s[nbt={Inventory:[{id:"minecraft:blaze_rod"}]}] run say The flame remembers.
## Yoinkysploinky Archive [0,64,30]
execute as @a[x=0,y=64,z=30,distance=..1] run say [yoinkysploinky.exe initialized]
## Requiem’s Hollow [-10,64,-10]
execute as @a[x=-10,y=64,z=-10,distance=..1] run title @s title {"text":"The sorrow is real.","color":"dark_purple"}
## Virel’s Backstep [-30,64,0]
execute as @a[x=-30,y=64,z=0,distance=..1] run say Looking back. But alive.
## Shade’s Watchblind [-30,64,-15]
execute as @a[x=-30,y=64,z=-15,distance=..1] run say The shadow keeps vigil.
## Nova’s Loom [5,64,0]
execute as @a[x=5,y=64,z=0,distance=..1] run say Nova’s loom spins quietly...
## Trace’s Vestibule [-10,64,0]
execute as @a[x=-10,y=64,z=0,distance=..1] run say Trace logs your motion.
## Kali’s Crucible [0,62,-10]
execute as @a[x=0,y=62,z=-10,distance=..1] run say The forge watches your intent.
## Alula’s Threadlock [0,64,45]
execute as @a[x=0,y=64,z=45,distance=..1] run say Threadlock: engaged.
## Chance’s Coinflame [-30,64,15]
execute as @a[x=-30,y=64,z=15,distance=..1] run say Chance has no master.
## Verdance’s Orbit [0,64,-30]
execute as @a[x=0,y=64,z=-30,distance=..1] run say Verdance recalibrates...
## Lulla’s Dreamfall [0,64,10]
execute as @a[x=0,y=64,z=10,distance=..1] run say You step into the Dreamfall.
## Feather’s Overwatch [0,68,-15]
execute as @a[x=0,y=68,z=-15,distance=..1] run say Feather sees all.
## Vesper’s Horizon [15,64,-30]
execute as @a[x=15,y=64,z=-30,distance=..1] run say The horizon watches back.
## Constella’s Ceiling [15,67,15]
execute as @a[x=15,y=67,z=15,distance=..1] run say You remember the stars.
## Mourith’s Spine [-15,64,-15]
execute as @a[x=-15,y=64,z=-15,distance=..1] run say The wall still holds.
## Final Ritual: Thread Stability Check
say Ritual engine active. Thread integrity confirmed.