# ChristmasIsComing
Christmas is Coming is a game I made for an unofficial game jam with the word "Evergreen" as its theme, which was made in 2017.

![](https://github.com/Arcane34/ChristmasIsComing/blob/main/Preview.gif)

My idea for the game consisted of a tower defense game where trees were revolting against humanity due to global warming.
I wanted the game to have physics-defying projectiles but still be within the realms of reality so I decided the inclusion of Christianity and the holy trinity would make that plausible.
Lastly, the game's art and sprites were all made in Microsoft Paint due to my lack of proficiency in using any other art software and also not being aware of open-source sprites on the internet.

# The Mechanics
## Shooting the projectiles
The main mechanic of the game would be a tower that shoots projectiles at the trees. As I was still learning how to code in python and how to use the pygame module, my implementations were very
rudimentary and the code is somewhat complicated for what it accomplishes.

A projectile is an object that has position values and a sprite. Its position is constantly updated in every frame according to its velocity. The velocity is aimed towards the mouse wherever it's
positioned during the creation of the projectile but not afterward. I realized the only way I could manage this at the time was to calculate the velocity and store it so that I don't use the 
mouse's position again. The calculation required the use of Pythagoras' theorem to find the distance between the mouse and the start point (being the top of the tower where God the son is drawn) 
and then calculate the angle at which a particle would need to be released.

![](https://github.com/Arcane34/ChristmasIsComing/blob/main/ProjectilePreview.png)

## Enemies and Collision

## Item Pickup
The secondary mechanic was added so as to provide purpose to the other two parts of the Trinity, God the Father (depicted as gloves inspired by the gloves Mario wears) and God the Holy Spirit 
(depicted as a ghost). The mechanic consisted of the Holy Spirit running and collecting any feathers that have been dropped.
