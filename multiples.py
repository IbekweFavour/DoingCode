number = 1024

if (number % 4 == 0):
	print("The number is a multiple of 4")
elif (number % 2 == 0):
	print("The number is not a multiple")



import java.util.Scanner;

public class NokiaApplication{
public static void main(String... args){

	Scanner input = new Scanner(System.in);
	

System.out.printf("%nWelcome to my Nokia 3310 Application%n");
System.out.print("""
	
1. Phone book
2. Messages	
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
	
""");
System.out.printf("%nNavigate to: ");
int phoneBook = input.nextInt();


switch(phoneBook){
case 1:

System.out.print("""
1. Search
2. Service Nos.
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
""");
break;
}

System.out.print("Enter the Options: ");
int option = input.nextInt();

switch(option){
case 1: System.out.print("""
 Search
""");
break;

case 2: System.out.print("""
 Service Nos.
""");
break;

case 3: System.out.print("""
 Add name
""");
break;

case 4: System.out.print("""
 Erase
""");
break;

case 5: System.out.print("""
 Edit
""");
break;

case 6: System.out.print("""
 Assign tone
""");
break;

case 7: System.out.print("""
 Send b'card
""");
break;

case 8:
System.out.print("""
	1. Type of view
	2. Memory status
""");
break;

case 9: System.out.print("""


 Sped dials
""");
break;

case 10: System.out.print("""
 Voice tags
""");
break;
}





}

}









//////////////////////////////////////////////////////////
System.out.print("Enter messages: ")
int messages = input.nextInt();
switch (messages){
case 2:
System.out.print("""
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Smileys
7. Message settings
}

System.out.print("Enter the message setting: ");
int messageSetting = input.nextInt();
	switch(messageSettings){
	1. Set 1
	1. Message centre number
	2. Messages sent as
	3. Message validity
	break;

	2. Common
		1. Delivery reports
		2. Reply via same centre
		3. Character support
	}
8. Info service
9. Voice mailbox number
10. Service command editior
""");
break;

case 3:
System.out.print("Nothing here.");


case 4:
System.out.print("""
1. Missed calls
2. Recieved calls
3. Dialled numbers
4. Erase resent call lists
5. Show call duration
	1. Last call duration
	2. All calls' duration
	3. Reckeved calls' duration
	4. Dialled calls' duration
	5. Clear timers
""");
break;


case 5:
System.out.print("""
1. Ringing tone
2. Ringing volumne
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warnings and game tones
8. Viberating alert
9. Screen saver
""");
break;


case 6:
System.out.print("""
1. Call settings
	1. Automatic redial
	2. Speed dialling
	3. Call wainint options
	4. Own number sending
	5. Phone line in use
	6. Automatic answer
2. Phone settings
	1. Language
	2. Cell info display
	3. Welcome note
	4. Network selection
	5. Lights
	6. Confirm SIM service actions
3. Security settings
	1. PIN code request
	2. Call barring service
	3. Fixed dialling
	4. Closed user group
	5. Phone security
	6. Change access codes

""");
break;


case 7:
System.out.print("Nothing to display");
break;


case 8:
System.out.print("Nothing to display");
break;


case 9:
System.out.print("Nothing to display");
break;


case 10:
System.out.print("Nothing to display");
break;


case 11:
System.out.print("""
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of data and time
""");
break;


case 12:
System.out.print("Nothing to display");
break;


case 13:
System.out.print("Nothing to display");
break;