# Computer Science

## contents
- [Computer Science](#computer-science)
  - [contents](#contents)
    - [Section 1 - Components of a computer](#section-1---components-of-a-computer)
    - [Section 2 - Systems software](#section-2---systems-software)
    - [Section 6 - Data types](#section-6---data-types)
    - [Section 7 - Arrays, tuples and records](#section-7---arrays-tuples-and-records)
    - [Section 8 - Boolean Algebra](#section-8---boolean-algebra)
    - [Section 9 - Legal, moral, ethical and cultural issues](#section-9---legal-moral-ethical-and-cultural-issues)
    - [Section 10 - Computational thinking](#section-10---computational-thinking)
    - [Section 11 - Programming techniques](#section-11---programming-techniques)


### Section 1 - Components of a computer
Address bus - For when CPU wants to access a specific memory location, gets the memory's address.
Data bus - Transmits data in memory between processor components and memory.
Control bus - Sends control signals. Bi-directional and ensures data and address bus dont conflict.
System bus - The three buses collectively connecting with a processor, I/O controller and memory.
Word - Fixed size of digits handled as a unit by a processor. Different processors have different word sizes.
Registers - Special memory cells operating at high speed. Store results of operations.
Accumulator(ACC) - Stores result of all calculations made by ALU.
Current Instruction register(CIR) -  Holds current instruction being executed, split into operand and opcode.
Memory Data Register (MDR) - Temporarily stores data read/written to memory.
Opcode - To determine the type of instruction and the hardware to execute it.
Operand - Holds either address of data, the actual data or the data to be operated on passed to ALU/ACC.
Clock - Switches between 1 and 0 millions of times per second generating signals.
Cache - Small, expensive, fast memory inside CPU. Instruction is copied to this.
Pipelining - Allows next instruction to be fetched whilst previous is being decoded to improve speed.
--------------------------------------------14/8/24-------------------------------------------------
Von Neumann Architecture - Specifies basic components in a computer
Hardvard architecture - Physically separate held memories for instructions. Used extensively with DSP systems.
Digital Signal Processing (DSP) - Include audio/speech, sonar and radar, biomedical, seismic and digital image processing.
Complex Instruction Set Computers (CISC) - Large sets using few lines of assembly code. Loads data into a separate register to perform function then stores it back into the original memory.
CISC Disadvantages - Many specialised instructions had to be built into hardware but only 20% were used.
CISC Advantages - Compiler has little work. Very little RAM required to store instructions.
Reduced Instruction Set Computers (RISC) - Only simple instructions that take one clock cycle can be executed.
RISC Disadvantages - Compiler has to do more work. More RAM required to store instructions.
RISC Advantages - One clock cycle so pipelining is possible. Four instructions execute as fast as one CISC.
Co-processor - An extra processor to supplement the CPU. Limited range of functions.
GPU - Graphics and image processing, has thousands of smaller cores for handling several tasks.
Multi-core CPU's - Significantly higher performance. Distribute workload effectively. Supercomputers
Barcodes - 2 Types, linear and QR codes. QR can hold more info.
Barcode readers - 4 types, pen-type readers, laser scanners, CCD readers and camera-based readers.
Pen-type readers - Light source and photo diode scan. Diode for light intensity and light for waveform. Small size, durable and simple design. Must touch the barcodChe to read.
Laser scanners - Laser beam and photo diode. Used in supermarkets commonly. Reliable and cheap.
Camera-based readers - Camera and processing method to decode. Can read on any surface, even if poorly printed
Camera-based readers uses - Phones for QR code scanning, Age verification, Couponing, Event ticketing.
Digital cameras (CCD) - Sensor with millions of tiny light sensors in a grid. Binary data is recorded so image can be reproduced on a computer software. Higher quality images but high power consumption.
--------------------------------------------15/8/24--------------------------------------------------
Radio Frequent Identification (RFID) - Using I/O, a Microchip with antenna. Used for tracking and identifying
Active tags - Have a battery, physically larger. Used to track things further away like cars.
Passive tags - Cheaper, no battery. Use radio waves for power, used in tagging items like groceries or cards.
Output devices - Take data by the computer and turn it into a way humans can read. Screens, printers etc.
LCD monitors (Liquid crystal display) - RGD diodes for each pixel. Usually back-lit with LED's.
LCD monitors advantages - Max brightness fast, sharp image, thin, last indefinetely, low power consumption.
LCD disadvantages - Slow to refresh, OLED's up to 200x faster. Hard to see at an angle, goes dark from side.
Organic LED screen(OLED) - Plastic screen so flexible. Can be used on almost any display.
OLED advantages - Much thinner, Brighter, consume less power, refresh fast, Colours clear at tighter angles.
OLED drawbacks - Dont last as long, wear out about 4x faster than LCD's. Very sensitive to water.
Laser printers - Use powdered ink called toner. Have cyan, magenta, yellow and black (CMYB) for colour.
Laser printers advantages - High-quality, high-speed. Becoming more affordable and used. Can do colour.
Laser printer disadvantage - For jobs other than text is limited by print quality, about 1200 dpi.
Inkjet printers - Spray small ink dots onto paper for an image. If High quality will produce excellent images.
Resolution - Based on DPI (dots per inch), the more dots the better.
Inkjet printers advantages - Cheaper than laser, High quality images with good paper, colour and resolution.
Inkjet printers disadvantages - Much slower, ink has to be replaced frequently.
Dot matrix / Impact printers - Print head has a matrix of pins which strike the paper through an inked ribbon.
Dot matrix benefits - Useful for multi-part stationary, can be used in dirty or damp areas.
Dot matrix drawbacks - Noisy, slow and poor print quality
3D printers - Can be used to create spare parts like car or aeroplane parts, medical eqpmt and prototypes etc.
Multimedia projectors - Used in classrooms for schools. More consistent as teacher just has to do lesson once.
Multimedia projectors adv - Before students crowded round a "16 screen, Chalkboards were used, Videos and images can improve learning and make it more interesting.
Computer speakers - Used in PC's, smartphones and portable devices as an inbuilt speaker for music, calls etc.
Actuators - Motors used with sensors to control something. e.g: Opening a window, start/stopping a pump etc.
--------------------------------------------16/8/24--------------------------------------------------
Secondary storage - Slower Storage for when power is off.
Hard disk - High capacity, rotating platters that spin with a drive head on the disk.
Optical disk - etiher CD-ROM, CD-R or CD-RW. Laser to burn disk to make areas less reflective. ROM has lands.
SSD - Array of chips on a board. Millions of NAND flash memory cells and a controller.
Virtual memory - If the RAM doesnt have enough storage.
Operating system - Programs that manage operations of the computer.
Operating system functions - Memory management, service routines, processor scheduling, I/O management etc.
Memory management - Every application/program run has to be allocated in memory whilst being used.
Paging - Memory divided into fixed sizes of 4KB each.
Segmentation - Logical division of addresses into varying length segments depending on the program structure.
Interrupts - Signal from program, hardware or clock to CPU. Happens when requesting services from OS or timer.
Interrupt service routines - Suspends programs to deal with interrupt. Different routine for each interrupt.
Types of interrupts - Power-fail interrupt (high priority), Clock interrupt, I/O device request (low pri)
Processor scheduling - OS can queue up the next process required to make efficient use of processor.
Multi-tasking - Single processor carries out small parts of multiple larger tasks in turn.
Scheduler - Ensures processor time is as efficient as possible.
Scheduler objectives - Maximise throughput, be fair to all users, good response time and keep hardware busy.
Round robin - Each process has a time slice. Time interval is set and moves on continuously if not complete.
First come first served - Jobs processed in order that they came.
Shortest remaining time - Program with the smallest estimated time to complete is run next.
Shortest job first - Process with the smallest estimated running time is run next. Similar to (one above).
Multi-level feedback queues - Several job queues, jobs can move between queues depending on time. To maximise processor use
Backing store management - Apps transfer from backing storage to memory when loaded. OS knows where free space is and keeps directory of where files are stored
Peripheral management - Managing I/O devies through their operation. e.g: Printers
Buffer - Memory where data goes so CPU can continue with another task. Compensates for speed difference
Distributed OS - Form of parallel processing where load is spread over multiple servers. Job is split and each small task is run on separate computers
Multi-tasking OS - Runs on a standalone computer. Several apps/programs running at once. e.g Music and work.
--------------------------------------------19/8/24--------------------------------------------------
Real-time OS - Must respond quickly to inputs, have a 'fail-safe', handle many inputs at once and have backup.
BIOS - For start-up. Loads OS from hard disk into RAM and tests hardware.
Device drivers - Provides a software interface to hardware. Allows OS to access hardware without knowing details of it.
Systems software - Needed to run hardware and application programs, such as OS, utility programs etc.
Utility software - To optimise performance, responsible for backing up files, compression, a firewall etc.
Disk defragmentation - Reorganises a magnetic disk so files which are split up are recombined in a series of blocks. Makes reading files quicker.
Applications software - Can be general-purpose, special-purpose or custom-written software
General-purpose software - Used for several purposes. e.g: Word processors and graphics packages
Special-purpose software - Performs a single specfic task/set of tasks.
Freeware - Software free to use but the user doesn't get access to source code.
Bytecode - Combines compiling and interpreting creates this.
Aspects of software development - Analysis, Design, Programming, testing, implementation and evaluation
Analysis - Includes the data, procedures, future plans and problems
Design - Includes processing, data structures, I/O, user interface, security and hardware
Black box testing - Carried out independently of code. Looks at program specification, covering all I/O's.
White box testing - Depends on code logic, derives from program structure.
Alpha testing - Carried out by software developers testing team. Reveals errors and unincluded items.
Beta testing - Giving package to potential users to use and get feedback so it can be modified further.
Implementation - When all testing is done software installed and more testing is done as new problems arise.
Evaluation - Assessed on effectiveness, usability and maintainability. Waiting period beforehand for users.
Waterfall Model - Review method where each step is completed one at a time. Can go back stages but have to work down through following stages
Spiral model - Review method, develops software in iterative stages. 
Agile modeling - Feedback at each part, changes made as next part of system is built. Prototype at each stage.
Extreme programming - Frequent releases of software made in short development cycles. Improves quality.
Agile modeling drawback - Abscence of user involvement
Agile modeling benefit - Suitable for small projects.
Extreme programming and RAD benefit - Good for large projects.
--------------------------------------------20/8/24--------------------------------------------------
Internet related algorithms - For huge data amounts on the Internet.
Route-finding algorithms - For GPS, finds shortest route
Compression algorithms - For compressing data files to transmit faster/use less space.
Encryption algorithms - Data sent online through purchases etc have to be encrypted.
Procedural languages - Has data structures like arrays, stacks and records.For languages like Python or Pascal
Polymorphism - A language's ability to process objects differently depending on their class.
Addressing mode - 2 digit code in the opcode of a machine code instruction
Immediate addressing - Operand is the actual value to be operated on
Direct addressing - Memory address of value
Indirect addressing - Location holding the address of the data
Indexed addressing - To access arrays. Gets operand address  by adding to the contents of the index register.
--------------------------------------------21/8/24--------------------------------------------------
Lossy compression - Info is removed from the file to reduce space.
Lossless compression - Removes info but copies it so it can be added back to the original file afterwards.
Run Length Encoding (RLE) - For images, doesnt record each pixel but just says how many of each colour per row. Shortens it
Plaintext - Data before it is encrypted
Ciphertext - The data after it has been encrypted
Cipher - Method of encryption used
Key - Code/info needed to lock/unlock authorisation to the message or data.
Vernam Cipher - Only cipher proven to be unbreakable. Key has to be longer than plaintext, random and used only once.
Symmetric encryption - Same key to encrypt and decrpyt data.
Asymmetric encryption - Public key to encrypt but private key only one person knows to decrypt.
Hashing - Provides a mapping between a random length input and a fixed length.
Hash total/Checksum - Value from unencrypted message data
Entity - Category of something thats of interest to an organisation about which data is to be recorded
--------------------------------------------------27/8/24----------------------------------------------
Flat file database - Only one file
Entity description - Written in format: Entity1 (Attribute1, Attribute2...)
Primary key - Name of the entity
Secondary key - For other attributes, another index in the database is created.
One-to-one - Entity relationship just between two things. (Wife and Husband)
One-to-many - Entity relationship between one thing and several. (Mother and children)
Many-to-many - Entity relation between many entities to many. (Student and course)
Entity relationship diagram - To represent relationship between entities in a database.
Foreign key - Links two tables in a relational database
Relational database - Separate tables are made for each entity. Data is ordered by shared attributes
Composite primary key - Primary key which has more than one attribute.
Referential integrity - Ensures a component isn't deleted if used in a table.
Normalisation - Process to find the best design possible for a database. Has three stages
Partial dependency - If any attributes depends on only part of a composite primary key, not fully.
SQL - Used for searching and updating tables using SELECT, FROM, WHERE.
Transaction processing - Capturing, selecting, managing and exchanging data
ACID - Atomicity, Consistency, Isolation, Durability. Ensures full transaction is done, not partly done.
ARPANET - US Defence project for communications without need for physical travel in 1960's
World Wide Web (WWW) - Collection of web pages on computers connected to the Internet
Internet - Network of networks to allow computer to communicate globally.
Sir Tim Berners-Lee - British scientist who developed the WWW. 
Internet Service Providers - Connect to cables along the sea to give internet connection locally.
Uniform Resource Locators - Address of a resource on the internet. Has location, method, host, resource etc.
Domain name - Identifies area that an internet resource is in. (.co.uk at end means its in the UK with 'co')
FQDN - Domain name but includes the host server name. (www or mail or ftp)
Physical topology - Actual design layout
Logical topology - Path the data travels in.
TCP/IP Protocol - Has application layer, transport layer, internet layer and link layer.
Firewall - Security blocking unauthorised access between two networks
Proxy server - Intercepts all packets going in/out of a network, and hiding the addresses for security.
HTML (HyperText Markup Language) - Language used for web pages. Makes structure and content of a web page
CSS (Cascade Style Sheets) - Dictates the style and formatting (visuals) of web pages. Used with HTML commonly
HTML div<> tag - Divides a page into separate areas, which can be referred to by name
CSS Identifiers - Defined with a # (#header)
Javascript - Script language. Interpreted and not compiled.

### Section 2 - Systems software


### Section 6 - Data types
Primitive data types - Provided by a programming language
-ibibyte - 1024 of the previous bytes instead of 1000


### Section 7 - Arrays, tuples and records
Array - Ordered, finite set of elements of the same type
Tuple - Ordered set of values of any type. Immutable so cannot be changed
Abstract data type - Created by the programmer instead of the language
Queues - List where items can only be retrieved at the front, and added on to the end, like a regular queue.
Dynamic data structure - Collection of data that can grow/shrink in size
Static data structure - Fixed in size, cannot inc/dec in size to free up space when running.
---------------------------------------------------3/9/24----------------------------------------------- 5 terms done ------
Priority queue - Queue but order is determined by the elements priority.
List - Abstract data type consisting of items that can be repeated.
Stacks - Items can only be modified from the top/front, like a stack of plates. (Undo and back buttons)
Overflow/Underflow - If the size exceeds maximum or goes below 0.
Hashing - Address is only a part of the full index. (453781 goes to address 781)
Dictionaries - Abstract data type consisting of keys and values. Each key has a value separated by a colon. (Name: "James")
Graphs - Set of nodes connected by edges or arcs.
Depth-first traversal - Go as far down a route as possible then backtrack to original point until all paths are done.
Breadth-first search - Visiting neighbours of each node, all nodes around first node then all nodes around second node.
Trees - Has a root, then branches and leaves. Root at the top and leaves at bottom, spreads out
Binary search tree - Each node has two children, splits into 2 each layer.

### Section 8 - Boolean Algebra
Logic circuits - Combining multiple logic gates (AND, OR, NOT) into one to form an output
De Morgan's first law - NOT(A OR B) == NOT A AND NOT B
De Morgan's second law - NOT(A AND B) == NOT A OR NOT B
XOR gate - Means exclusive OR. Has to be an OR, if both are true its false, only ONE has to be true.
D-type flip-flop - Positive edge triggered flip-flop, can only change from 1 to 0.

### Section 9 - Legal, moral, ethical and cultural issues
Data Protection Act 1998 - Anyone with personal info must keep it secure and its under their responsibility. Must have security
Computer misuse act 1990 - Computers are not to be used to perform or be involved in malware attacks of any sort.
Copyright Designs and Patents Act 1998 - Ensures no data cannot be copied/taken without permission from the original creator.
Regulation of Investigatory Powers Act 2000 - Allows public bodies to carry out surveillance and investigation for protection.
Internet censorship - Control of what can be accessed/viewwed. Can be carried out by governments, individuals or private firms.
Trolls and Cyber-bullying - Have become more common on the internet, and dangerous internet groups such as ISIS formed.


### Section 10 - Computational thinking
Computational thinking - Form the problem as a computational problem and then form an algorithm to solve it.
Data abstraction - How the data represented is understood by the computer is hidden.
Caching - Temporary store of programs used that may need to be used again frequently or shortly
Procedural abstraction - Similar to a function, using a procedure to carry out an algorithm. Programmar just needs to call this.
Structured approaches - More clarity and maintainability. Selection, sequence, iteration.
Block-structured languages - Only need three control structures (Sel, Seq, It) such as Python and Pascal
Trace tables - Allows you to follow an algorithm line by line to test it.
Parallel computing - Several processors running several programs at once
Concurrent processing - One at a time, each processor given a slice of processing time then it keeps flowing.
Exhaustive search - Trying all possible solutions until one is found
Backtracking - Trying out different sequences until finding a solution (A maze is a good example)


### Section 11 - Programming techniques
Exponention - Written as **. 2² = 2 ** 2
Comments - For leaving notes in the code to help understand the pseudocode behind it, how it works.
Constants - Value never changes whilst program is running.
Relational operators - In a selection sequence, depends on a condition (>=, >, <, ==, !=)
Switch/case statement - Alternative to a nested if statement, gives the user options to pick from
Subroutines - Functions or procedures, block of code that can be called
Parameters passed by value - In Python, the value of the local variable is passed to function as its declared outside the func.
Parameters passed by reference 
Recursive subroutines - Defined in terms of itself
IDE - Integrated Development Environment (Visual Studio is an IDE)
IDE features - Create new files/programs, running and compiling the code, debugging, colour coded, code completion, VCI (Github)
Normal data - Data within the range you expect and the data type you expect. Nothing wrong with it.
Boundary data - Data thats just on the valid boundaries, any more/less wouldn't be valid
Erroneous data - Data that is outside the range or is the wrong data type. Produces an error
Dry-run test - Done by using a trace table to note the logic of the code line by line.
Object oriented programming - Uses only objects, they interact and communicate to work
Object features - Every object has a state (on/off), attributes and behaviours
Class - Blueprint or template for an object
**(A)**Encapsulation - For large projects, coders dont have to worry about how other parts of the system affect any of their new code. Subroutines can be tested even if global variables have the same name.
Time complexity - How long an algorithm takes to solve
Permutations -  Total number of possible combinations/arrangements of objects
Linear search - Goes through one by one until found
Binary search - Repeatedly halving the list whilst keeping the side with the target item in until its found.
Tree binary search - Root is examined and then tree is halved by the roots instead, until item is found down the tree
Bubble sort - Largest item bubbles its way to the top, repeats until in order.
Insertion sort - Item is inserted into the mini-list where it belongs, mini-list starts at 2 and adds one item per pass.
Merge sort - Divide and conquer method. Splits list until each item is separate then exponentially grows (doubles by merging)
**(A)**Quick sort - Choose a random number as a pivot, split with numbers less than it before and numbers greater than it after as 2 lists, then repeat with 2 pivots to sort.
Dijkstra's algorithm - Finds shortest path from one node to all other nodes. (A to B, A to C, A to D)
