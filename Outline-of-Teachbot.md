# Teacherbot Overview
This document is an overview of the how the teacherbot will function and who will be designated to create each function of the bot.

* [X] Create Github repository | **Ryan**
* [ ] Implement a mechanism to take attendance through Discord
* [ ] Implement the "pods" that Dr. Neat wants
* [ ] Create some type of website interface so that Dr. Neat can see who's been present and who has not

## Mechanism to Take Attendance
The teacherbot will take attendance by sending a message to a designated channel which will have a reaction which students can react to mark themselves as present.  There will be a reaction for each of Dr. Neat's periods and students will react to the corresponding one to mark themselves present.  As a simple hypothetical, if Dr. Neat has periods 1, 2, 3, 4, and 5 then the bot will react to the attendance message with the emojis 1️⃣, 2️⃣, 3️⃣, 4️⃣, and 5️⃣.  Students in period 1 will mark themselves present by reacting to the 1️⃣ emoji and student in period 2 will mark themselves as present by reacting to the 2️⃣ emoji and so on for every student of each of Dr. Neat's periods.  Each day this message will be resent (the old message will probably be deleted) and students will have to react once again to mark themselves as present.
After an initial version is working there will be two goals to make the method even better. These goals are discussed below
### Autodetect Which Periods Are Today
This will allow the attendance function to automatically know which days are periods 1, 2, and 3 and which days are periods 2, 4, and 6.  One approach to get this behavior is to use the information in the calendar on the GUSD CVHS website to determine which days correspond to which periods.  If parsing the information fails for whatever reason then the bot will send a message to Dr. Neat asking him to manually set the periods for that day.
### Automatically Take Attendance Through the GUSD Website
Another feature of the bot that would make it really helpful to Dr. Neat would be an ability for it to be able to take attendance through the GUSD attendance website.  It would login using Dr. Neat's credentials and take attendance mimicking how he would take attendance.
