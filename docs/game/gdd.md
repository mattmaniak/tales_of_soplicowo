# Tales of Soplicowo
## Game Design Document
by Mateusz Maniak

## Table of Contents
- [Overview](#overview)  
  1. [Motto](#motto)  
  2. [Logline](#logline)  
  3. [Genre](#genre)  
  4. [Objective](#objective)  
  5. [Setting](#setting)  
  6. [Plot](#plot)  
  7. [Inspirations](#inspirations)  
  8. [Unique Selling Point](#unique-selling-point)  
- [Development](#development)
  1. [Technologies](#technologies)  
  2. [Assets Budget Summary](#assets-budget-summary)  
- [Characters](#characters)  
  1. [Player](#player)  
  2. [NPCs](#npcs)  
- [World](#world)  
  1. [Map](#map)  
  2. [Levels](#levels)  
- [Gameplay](#gameplay)  
  1. [Core Gameplay Loop](#core-gameplay-loop)
  2. [Core Number](#core-number)
  3. [MoSCoW analysis of mechanics](#moscow-analysis-of-mechanics)
  4. [Prizes](#Prizes)
  5. [Statistics of the Player](#statistics-of-the-player)
- [Story](#Story)
  - [Quests and their IDs](#quests-and-their-ids)  
- [Graphics](#graphics)  
- [Sound](#sound)  
  1. [Sound Effects](sfx)  
  2. [Music](#music)  
- [Accessibility](#accessibility)  

## <a id='description'></a>Description
1. ### <a id='motto'></a>Motto
   Unite them all/Fight with word like a sword/Unite with word, not a sword.

2. ### <a id='logline'></a>Logline
   Play as a 19th-century priest whose goal is to reunite Polish noble-class in order to prepare uprising against Russian. Use word as a sword and try to persuade them. Will you succeed?

3. ### <a id='genre'></a>Genre
   Adventure RPG.

4. ### <a id='objective'></a>Objective
   Do some open-source in game development.

5. ### <a id='setting'></a>Setting
   Soplicowo.

6. ### <a id='plot'></a>Plot
   Taduesz backs to Soplocowo from Vilnus. This causes the castle conflict again. His father - Priest Robak has to help Soplicas get the castle. However, some things go wrong during his journey and Horeszkos' are preparing some big too.

7. ### <a id='inspirations'></a>Inspirations
   "Don't be told what games must be. Instead find new and different types of games."  
   Hideo Kojima

   As the title suggests, those are only inspirations and won't be copied directly. It's just a list of key elements those seem to be fitting to our idea.
   - *AER Memories of Old* - minimalistic graphics with faceless characters.
   - *Disco Elysium* - engaging dialogue trees instead of combat.
   - *Hellblade: Senua's Sacrifice* - personal narrator, environmental puzzles.
   - *Horizon Zero Dawn* - specific save points (campfires).
   - *The Witcher 2: Assassins of Kings* - small but dense atmospheric Slavic-based world.

## <a id='development'></a>Development
1. ### <a id='technologies'></a>Technologies
   The newest Python 3.8/3.9, Panda3D engine with it's RenderPipeline.
2. ### <a id='assets-budget-summary'></a>Asset Budget Summary
   The less the better.

## <a id='characters'></a>Characters
Every character should be somehow archetypic.

1. ### <a id='player'></a>Player
   - **Father Robak** a.k.a. **Jacek Soplica** - a catholic priest, ex-vagrant.
2. ### <a id='npcs'></a>NPCs
   - **Protazy Brzechalski**
   - **Tadeusz Soplica** - title character
   - **Judge Soplica** - mentor archetype - conservative Pole stereotype.
   - **Jankiel** - local Jew.
   - **Telimena** - seductress archetype - *femme fatale*.
   - **Zosia Horeszko** - maiden archetype - Tadeusz's crush.
   - **Gerwazy Rębajło**
   - **Count Horeszko** - Dandelion from *The Witcher*.
   - **Major Płut** - Russian officer of Polish descent.
   - **Count's Jockeys** - two French-like horsemen.

## <a id='world'></a>World
Closed but with various options to achieve a destination. Internal legacy prototype `mapa_w_skali_v2.jpg` is a good initial reference for a level design.

1. ### <a id='map'></a>Map
   Contains some levels on the single map. It will be important storytelling and reputation system component too - some places will be unavailable, while other will be available according to the player choices. This will provide gameplay nonlinearity.
2. ### <a id='levels'></a>Levels
   - Level 1
   - Level 2.

## <a id='gameplay'></a>Gameplay
The player acts as a priest whose goals is to go through the quests which are strictly related with Polish noble-class and *Sir Thaddeus* events. The goal is to persuade them to reunion. It will be done via helping them during various tasks from the Mickiewicz's book and deep talks about the Commonwealth. Optionally, the player will have to find and repair chapels. To solve those problems, player will have to explore levels and solve engaging puzzles.

1. ### <a id='core-gameplay-loop'></a>Core Gameplay Loop
   1. Enter and explore level a little.
   2. Deep talk with quest owner who explains the problem. 
   3. Go to a specified place to find a solution.
   4. Solve environmental puzzles and optionally fix chapel.
   5. Short talk with NPC that thanks for the help and informs about a next job.

2. ### <a id='core-number'></a>Core Number
   Core number of the game should be 2 multiplications to symbolise a dualism everywhere, eg. there should be two ways to get into an area, two dialogue answers...

3. ### <a id='moscow-analysis-of-mechanics'></a>MoSCoW analysis of mechanics:
   - **Must have**:
     - High third-person perspective camera with a fixed pitch angle.
     - Comperhensive dialogue trees with short dialogues.
     - Reputation system.
     - Detailed and dense world.
     - Courier's backpack when carrying repair tools.
     - Auto save during specific story moments.
     - *Press any button to continue* after loading screens.
   - **Sould have**:
     - Day-night cycle.
     - All unique *Sir Thaddeus* characters.
     - In-door visibility - transparent portal on player or buildings half-transparency.
     - Basic in-game menu with: map, reputation graph, skills and current quest description.
     - Graphical hints, meaningful icons, GIFs representing various settings...
   - **Could have**:
     - Basic economy for repair stuff trade.
     - Compass.
     - Time skip only near repaired chapels.
     - Chapels repair and manual save possibility near them.
   - **Won't have**:
     - Shoulder third-person perspective camera.
     - Minimap.
     - Combat.
     - Stealth.
     - Random encounters.

4. ### <a id='prizes'></a>Prizes
   Story-related.

5. ### <a id='statistics-of-the-player'></a>Statistics of the Player
   The game shouldn't be explicit with stats displaying them by numbers. Instead, it should use some graphs and mainly storytelling to show characters' parameters. Here comes the *show, don't tell* rule.

## <a id='Story'></a>Story
There is no distiction between and side jobs to simplify implementation. There will be only nonlinear main quests whose will have optional tasks sometimes to provide more diverse choices and consequences.
- ### <a id='quests-and-their-ids'></a>Quests and their IDs
  0. Deeply engaging guest.

## <a id='sound'></a>Sound
1. ### <a id='sfx'></a>Sound Effects
   Simple free assets.
2. ### <a id='music'></a>Music
   Some tracks. Must be interactive and adaptive as games are interactive medium.

## <a id='graphics'></a>Graphics
3D low poly pixel art, where pixels are used only for details. Meshes and the textures' context are classicaly flat. Rich post-processing can be easily achieved due the Render Pipeline.

## <a id='accessibility'></a>Accessibility
Each in-game feedback is expressed via at least two sensitive events, eg. dialogues use subtitles and narrator, enemies distraction - some character outline and a proper sound. Visual effects change it's shape, not color only to provide meaningful experience also for color-blind people. Most of the information is shown using mix of various visual and sound effects.
