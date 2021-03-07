# Tales of Soplicowo
Adventure RPG video game
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
  2. [Levels and their IDs](#levels-and-their-ids)  
- [Gameplay](#gameplay)  
  1. [Core Gameplay Loop](#core-gameplay-loop)
  2. [Core Number](#core-number)
  3. [MoSCoW analysis of mechanics](#moscow-analysis-of-mechanics)
  4. [Prizes](#Prizes)
  5. [Enjoyable Failures](#enjoyable-failures)
  6. [Statistics of the Player](#statistics-of-the-player)
- [Story](#Story)
  - [Events/Books](#events-books)  
  - [Quests and their IDs](#quests-and-their-ids)  
  - [Endings and their IDs](#endings-and-their-ids)  
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
   ~Hideo Kojima

   As the title suggests, those are only inspirations and won't be copied directly. It's just a list of key elements those seem to be fitting to our idea.
   - *AER Memories of Old* - minimalistic graphical design with faceless characters.
   - *Disco Elysium* - engaging dialogue trees instead as a combat.
   - *Hellblade: Senua's Sacrifice* - environmental puzzles and personal narration.
   - *Horizon Zero Dawn* - specific save points only.

## <a id='development'></a>Development
1. ### <a id='technologies'></a>Technologies
   The newest Python 3.8/3.9, Panda3D engine with it's RenderPipeline.
2. ### <a id='assets-budget-summary'></a>Asset Budget Summary
   The less the better.

## <a id='characters'></a>Characters
There should be 12 characters, excluding the players. Each of them should be connected with exactly of the 12 Jungian archetypes. One of them will by same as the player's archetype as opposition.

1. ### <a id='player'></a>Player
   - **Father Robak** a.k.a. **Jacek Soplica** - a catholic priest, ex-vagrant.
2. ### <a id='npcs'></a>NPCs
   Every of them will be at least neutral on unfriendly. There will be a possibility to gain some friendship relations according to player's decisions.
   - #### Soplicas
      - **Protazy Brzechalski**.
      - **Tadeusz Soplica** - title character
      - **Judge Soplica** - mentor archetype - conservative Pole stereotype.

   - #### Horeszkos
      - **Count Horeszko** - Dandelion from *The Witcher*.
      - **Zosia Horeszkówna** - maiden archetype - Tadeusz's crush.
      - **Gerwazy Rębajło**.

   - #### Russians
      - **Major Płut** - Russian officer of Polish descent.
      - **Captain Nikita Rykow**.

   - #### Dobrzyńscy
      - **Maćko Dobrzyński**.
      - **Bartek Brzytewka**.

   - #### Neutral
      - **Jankiel** - local Jew.
      - **Telimena** - seductress archetype - *femme fatale*.

## <a id='world'></a>World
Closed but with various options to achieve a destination. Internal legacy prototype `mapa_w_skali_v2.jpg` is a good initial reference for a level design. It should be full of symbols to communicate effectively.

1. ### <a id='map'></a>Map
   Contains some levels on the single map. It will be important storytelling and reputation system component too - some places will be unavailable, while other will be available according to the player choices. This will provide gameplay nonlinearity. Each level will be symbolic and will be uniqely different.

2. ### <a id='levels-and-their-ids'></a>Levels and their IDs
   0. Soplicowo - starting point, hub world, maybe.
   1. Horeszko's Castle.
   2. Forest.
   3. Jankiel's Inn.
   4. Another forest.
   5. Horeszko's Castle.
   6. Soplicowo.
   7. Horeszko's Castle.
   8. Dobrzyn.
   9. Sopliciwo.
   10. Dobrzyn.
   11. Soplicowo - ending point.

## <a id='gameplay'></a>Gameplay
The player acts as a priest whose goals is to go through the quests which are strictly related with Polish noble-class and *Sir Thaddeus* events. The goal is to persuade them to reunion. It will be done via helping them during various tasks from the Mickiewicz's book and deep talks about the Commonwealth. Optionally, the player will have to find and repair chapels.

To solve those problems, player will have to explore levels those will be labirynths with various paths to go through. They will be somehow connected with a camera's fixed pitch and base on the problem of getting into some kind of relatively complex place.

Note that each further labirynth and dialogue should be harder to provide a customizable progression system with a progressive difficulty.

The gameplay will be a little modular only, as there will be labirynth and NPCs conversations as the cores. These mechanics modules will overlap.

Both mechanics will be expressive for the player by their nonlinearity, so the player will be able to choose own way and behave in-game as he/she intends.

It will be somehow mix of systemic and directed approach: on the one hand, it will allow player to use mechanics on their own, like various exploration possibilities and dialogue choices, on the other hand, the game won't have much mechanics (above two only) so the directed approach will be present too.

1. ### <a id='core-gameplay-loop'></a>Core Gameplay Loop
   Core but high-level. Maybe a separate low-level description is needed too.
   1. Enter and explore level a little.
   2. Deep talk with quest owner who explains the problem. 
   3. Go to a specified place to find a solution.
   4. Find a path through a labirynth and optionally fix chapel.
   5. Short talk with NPC that thanks for the help and informs about a next job seamlessly.

2. ### <a id='core-number'></a>Core Number
   Core number of the game should be 2 multiplications to symbolise a dualism everywhere, eg. there should be two ways to get into an area, two dialogue answers...

3. ### <a id='moscow-analysis-of-mechanics'></a>MoSCoW analysis of mechanics:
   - **Must have**:
     - High third-person perspective camera with a fixed pitch angle.
     - Comperhensive dialogue trees with short dialogue lines.
     - Reputation system.
     - Detailed and dense world.
     - Auto save during specific story moments.
     - *Press any button to continue* after loading screens.
   - **Sould have**:
     - Day-night cycle that changes gameplay and mostly negative night consequences.
     - In-door visibility - transparent portal on player or buildings half-transparency.
     - Basic in-game menu with: map, reputation graph, skills and current quest description.
     - Symbolic hints: icons, GIFs, sounds to represent settings differences and visualise invisible.
     - Compass.
   - **Could have**:
     - Basic economy for repair stuff trade.
     - Time skip only near repaired chapels.
     - Chapels repair and manual save possibility near them.
     - Courier's backpack when carrying repair tools.
   - **Won't have**:
     - Shoulder third-person perspective camera.
     - Minimap.
     - Combat.
     - Stealth.
     - Random encounters.
     - All unique *Sir Thaddeus* characters.

4. ### <a id='prizes'></a>Prizes
   If a player will explore levlels enough, there will be a chance to find something that will enhance the historical lore and/or add additional dialogue.

5. ### <a id='Enjoyable Failures'></a>Enjoyable Failures
   It's inevitable that a player could get lost, however this particular scenario will be quite similar to the deep exploration - sometimes additional content will be found and sometimes clues how to get back and find a proper way.

6. ### <a id='statistics-of-the-player'></a>Statistics of the Player
   The game shouldn't be explicit with stats displaying them by numbers. Instead, it should use some graphs and mainly storytelling to show characters' parameters. Here comes the *show, don't tell* rule.
   
   Optionally, there will be a reversed triangle that symbolises main character's attitude. Center will be the initial neutrals state. Left corner will symbolise Horeszko family, while right one - Soplicas. Collaboration with Russians will be placed at the bottom. As the protagonist is one of the Soplicas, player's attitude may be prejudiced, however to reconceal noblemen and thus succeed, neutrality will be necessary. Those attitudes will be the essence of the RPG loyality system, however it may judge player's morality so it should be considered deeply before optional implementation. This would trick player as working with Soplicas will be suggested at first sight, even if they won't be too familiar. Because of that, player probably will try to become neutral, and tho will probably achieve a relative success. 

## <a id='Story'></a>Story
There is no distiction between and side jobs to simplify implementation. There will be nonlinear main quests only whose will have optional tasks sometimes to provide more diverse choices and consequences.

- ### <a id='events-books'></a>Events/Books
  1. Tadeusz arrives to Soplicowo, and Priest Robak later on.
  2. Count Horeszko arrives to a Castle and stalks Zosia, Robak comes in-between.
  3. Mushrooming with Soplicas.
  4. Robak encourages noblemen in Jankiel's Inn to reconceal, then helps with a  Bear hunting.
  5. Robak gifted with the Bear meat, serious argument in the Castle.
  6. Priest arrives to Soplicowo once again, then to the Castle.
  7. Robak tries to track Gerwazy to Dobrzyn (not included in the source).
  8. Priest Robak arrives back to Soplicowo and makes a coming out to Judge.
  9. Dobrzyn noblemen captive Soplicas, Robak goes to there and back with Maćko Dobrzyński is wounded nearly after in a Battle with Russians.
  10. Public coming out and death of Robak, talks about emigration.
  11. Public rehabilitation of Jacek Soplica in 1812 by Podkomorzy, during Napoleon's raid on Russia.
  12. Junket with Polish generals in Sopliciwo, Tadeusz and Zosia wedding, a hope.

- ### <a id='quests-and-their-ids'></a>Quests and their IDs
  0. Some kind of intuitive and immersive tutorial to provide an **intro**.
  1. A little harder quest to create an **exposition** and speed-up **pacing**.
  2. Harder quest with a **rising action**.
  3. Final hard quest that becomes a **climax**.
  4. A slowdown and player's Catharsis.
  5. A short cutscene/gameplay event as a final conclusion. 

- ### <a id='endings-and-their-ids'></a>Endings and their IDs
  0. The Blind One - Soplicas.
  1. The Lawful Harsh - Horeszkos.
  2. The Collaborant - Russians.
  3. The Reconciler - active neutrality.

## <a id='sound'></a>Sound
1. ### <a id='sfx'></a>Sound Effects
   Simple free assets.
2. ### <a id='music'></a>Music
   Some tracks. Must be interactive and adaptive as games are interactive medium.

## <a id='graphics'></a>Graphics
3D low poly pixel art, where pixels are used only for details. Meshes and the textures' context are classicaly flat. Rich post-processing can be easily achieved due the Render Pipeline.

## <a id='accessibility'></a>Accessibility
Each in-game feedback is expressed via at least two sensitive events, eg. dialogues use subtitles and narrator, enemies distraction - some character outline and a proper sound. Visual effects change it's shape, not color only to provide meaningful experience also for color-blind people. Most of the information is shown using mix of various visual and sound effects. Also the game should support at least custom mappings for: keyboard + mouse and Xbox, PlayStation pads. Game controls should be as much analogue as possible, eg. triggers on pads. The game should contain full colorblind-friendly only visuals optionally.
