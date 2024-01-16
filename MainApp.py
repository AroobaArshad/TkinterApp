#Importing the tkinter module
from tkinter import *
#Importing pillow library for the images
from PIL import ImageTk, Image
#Importing the messagebox module to use messagebox
from tkinter import messagebox
import requests
#Importing module for randomization
import random
from random import shuffle
#Importing module for html escape
import html
#Importing pygame for sound effects
import pygame

#Initializing pygame
pygame.init()

#Represents a quiz question along with associated attributes
class Quiz_Question:

    def __init__(self, question: str, correct_answer: str, quiz_choices: list):
        self.question_text = question
        self.correct_answer = correct_answer

        #Iniatializing the list of choices for the questions
        self.quiz_choices = quiz_choices

class Quiz_Logic:

    #Iniatializing the variables during the quiz state
    def __init__(self, questions):
        self.question_number = 0   #Tracking the current question number
        self.score = 0   #Tracking the user's score
        self.questions = questions   #Storing the list of questions
        self.present_question = None   #Storing the current question
        self.right_answers_given = 0   #Tracking the number of correct answers

    #Checking for more questions in the quiz
    def if_questions_more(self):
        return self.question_number < len(self.questions)
    
    #Updating the current question
    def successor_question(self):
        self.present_question = self.questions[self.question_number]
        self.question_number += 1
        text_Q = self.present_question.question_text
        return f"Q.{self.question_number}: {text_Q}"
    
    #Updating the score when the user's answer matches the correct answer
    def answer_checking(self, answer_by_user):
        correct_answer = self.present_question.correct_answer
        if answer_by_user.lower() == correct_answer.lower():
            self.right_answers_given += 1
            return True
        else:
            return False
        
    #Calculating and returning the user's score
    def calculate_score(self):
        wrong = self.question_number - self.right_answers_given
        percentage_score = int(self.score/self.question_number * 100)
        return (self.score, wrong, percentage_score)
    

#--------------------------------------------------------------------# 
#----- Class that represents the start screen of the trivia app -----#
#--------------------------------------------------------------------# 
class FirstScreen:

    def __init__(self, root):
        #Initializing the first screen and it's layout
        self.root = root
        self.root.title("Quiz Time")
        self.root.geometry("820x520+200+30")
        self.root.resizable(0, 0)
        self.root.iconphoto(False, ImageTk.PhotoImage(file = "Images/8587213.png"))

        #Creating a frame within the root window
        self.frame1 = Frame(self.root, width = 820, height = 520)
        self.frame1.pack()

        #Setting a background image
        self.Img = Image.open("Images/startscreen.png")
        self.ResizeImg = self.Img.resize((840, 590)) #Resizing the image
        self.NewImg = ImageTk.PhotoImage(self.ResizeImg)
        self.Image1 = Label(self.frame1, image = self.NewImg, bd = 0)
        self.Image1.place(x = 0, y = 0)

        #Image for play button
        self.Img2 = Image.open("Images/Untitled design (1).png")
        self.ResizeImg2 = self.Img2.resize((130, 60)) #Resizing the image
        self.NewImg2 = ImageTk.PhotoImage(self.ResizeImg2)

        self.play_btn = Button(self.frame1, image = self.NewImg2, padx = 20, pady = 4,
                               command = self.quiz_start, borderwidth = 0)
        self.play_btn.place(relx = 0.5, rely = 0.72, anchor = CENTER)

    def quiz_start(self):
        #Destroying the instance of the first screen
        self.frame1.destroy()

        #Creating an instance of SelectCategory
        select_category = SelectCategory(self.root)


#---------------------------------------------------------------------------------# 
#----- Class that represents the category selection screen of the trivia app -----#
#---------------------------------------------------------------------------------# 
class SelectCategory:

    def __init__(self, root):
        #Initializing the category selection screen and it's layout
        self.root = root
        self.root.title("Category Selection")
        self.root.geometry("840x580+200+30")

        #Creating a frame within the root window
        self.frame2 = Frame(self.root, width = 840, height = 590)
        self.frame2.pack()

        #Setting a background image
        self.Img = Image.open("Images/Untitled design (2).png")
        self.ResizeImg = self.Img.resize((840, 580)) #Resizing the image
        self.NewImg = ImageTk.PhotoImage(self.ResizeImg)
        self.Image1 = Label(self.frame2, image = self.NewImg, bd = 0)
        self.Image1.place(x = 0, y = 0)

        self.label2 = Label(self.frame2, text = "Choose a Category!", bg = "#FFF6EF",
                            font = ("Comic Sans MS", 26, "bold"))
        self.label2.place(relx = 0.5, rely = 0.09, anchor = CENTER)

        #Creating a variable to store the selected category
        self.category_selected = StringVar()

        #Creating buttons for selecting categories with specific commands

        #Images for different categories
        self.manImg = Image.open("Images/4.png")
        self.manResizeImg = self.manImg.resize((160, 160)) #Resizing the image
        self.manNewImg = ImageTk.PhotoImage(self.manResizeImg)

        self.btn1 = Button(self.frame2, image = self.manNewImg, borderwidth = 0, bg = "#FFF6EF",
                           command = lambda: self.select_category("Entertainment: Japanese Anime and Manga"))
        self.btn1.place(x = 60, y = 110)

        self.bookImg = Image.open("Images/7.png")
        self.bookResizeImg = self.bookImg.resize((160, 160)) #Resizing the image
        self.bookNewImg = ImageTk.PhotoImage(self.bookResizeImg)

        self.btn2 = Button(self.frame2, image = self.bookNewImg, borderwidth = 0, bg = "#FFF6EF",
                           command = lambda: self.select_category("Entertainment: Books"))
        self.btn2.place(x = 250, y = 110)

        self.filmImg = Image.open("Images/5.png")
        self.filmResizeImg = self.filmImg.resize((160, 160)) #Resizing the image
        self.filmNewImg = ImageTk.PhotoImage(self.filmResizeImg)

        self.btn3 = Button(self.frame2, image = self.filmNewImg, borderwidth = 0, bg = "#FFF6EF",
                           command = lambda: self.select_category("Entertainment: Film"))
        self.btn3.place(x = 440, y = 110)

        self.artImg = Image.open("Images/8.png")
        self.artResizeImg = self.artImg.resize((160, 160)) #Resizing the image
        self.artNewImg = ImageTk.PhotoImage(self.artResizeImg)

        self.btn4 = Button(self.frame2, image = self.artNewImg, borderwidth = 0, bg = "#FFF6EF",
                           command = lambda: self.select_category("Art"))
        self.btn4.place(x = 620, y = 110)

        self.celImg = Image.open("Images/6.png")
        self.celResizeImg = self.celImg.resize((160, 160)) #Resizing the image
        self.celNewImg = ImageTk.PhotoImage(self.celResizeImg)

        self.btn5 = Button(self.frame2, image = self.celNewImg, borderwidth = 0, bg = "#FFF6EF",
                           command = lambda: self.select_category("Celebrities"))
        self.btn5.place(x = 60, y = 290)

        self.spImg = Image.open("Images/1.png")
        self.spResizeImg = self.spImg.resize((160, 160)) #Resizing the image
        self.spNewImg = ImageTk.PhotoImage(self.spResizeImg)

        self.btn6 = Button(self.frame2, image = self.spNewImg, font = ("corbel", 16), borderwidth = 0, bg = "#FFF6EF",
                           command = lambda: self.select_category("Sports"), padx = 0, pady = 0)
        self.btn6.place(x = 250, y = 290)

        self.genImg = Image.open("Images/2.png")
        self.genResizeImg = self.genImg.resize((160, 160)) #Resizing the image
        self.genNewImg = ImageTk.PhotoImage(self.genResizeImg)

        self.btn7 = Button(self.frame2, image = self.genNewImg, borderwidth = 0, bg = "#FFF6EF",
                           command = lambda: self.select_category("General Knowledge"))
        self.btn7.place(x = 440, y = 290)

        self.carImg = Image.open("Images/3.png")
        self.carResizeImg = self.carImg.resize((160, 160)) #Resizing the image
        self.carNewImg = ImageTk.PhotoImage(self.carResizeImg)

        self.btn8 = Button(self.frame2, image = self.carNewImg, font = ("corbel", 16), borderwidth = 0, bg = "#FFF6EF",
                           command = lambda: self.select_category("Entertainment: Cartoons and Animations"))
        self.btn8.place(x = 620, y = 290)

        #Back and Next buttons

        self.nextImg = Image.open("Images/Untitled design (3).png")
        self.nextResizeImg = self.nextImg.resize((140, 50)) #Resizing the image
        self.nextNewImg = ImageTk.PhotoImage(self.nextResizeImg)

        self.next_btn = Button(self.frame2, image=self.nextNewImg, bg = "#FFF6EF",
                               font = ("corbel", 16), borderwidth=0,
                               command = self.show_info)
        self.next_btn.place(relx = 0.5, rely = 0.86, anchor = CENTER)

        self.back_btn = Button(self.frame2, text = "<  Back", borderwidth = 0,
                               font = ("corbel", 20), bg = "#FFF6EF",
                               command = self.go_back)
        self.back_btn.place(relx = 0.12, rely = 0.1, anchor = CENTER)

    def go_back(self):
        #Destroying the instance of the current screen
        self.frame2.destroy()

        #Creating an instance of the initial screen
        initial_screen = FirstScreen(self.root)

    #Method to handle the selected buttons
    def select_category(self, category):
        #Setting the selected category
        self.category_selected.set(category)

        #Changing the borderwidth of the selected button and resetting others
        mapping_buttons = {
            "Entertainment: Japanese Anime and Manga": self.btn1,
            "Entertainment: Books": self.btn2,
            "Entertainment: Film": self.btn3,
            "Art": self.btn4,
            "Celebrities": self.btn5,
            "Sports": self.btn6,
            "General Knowledge": self.btn7,
            "Entertainment: Cartoons and Animations": self.btn8
        }

        for button_category, button in mapping_buttons.items():
            if button_category == category:
                button.config(borderwidth = 3, relief = RAISED)
            else:
                button.config(borderwidth = 0)

    #Method for displaying selected category's inormation
    #Method to transition to the difficulty choosing screen
    def show_info(self):
        category = self.category_selected.get()

        #Displaying error message if no category is chosen
        if not category:
            messagebox.showerror("Error", "Please choose a category first.")
            return
        
        explanation = self.get_category_explanation(category)

        #A Toplevel window that displays the category information
        info_box = Toplevel(self.root)
        info_box.title("Category Explanation")
        info_box.geometry("400x320+410+150")
        info_box.resizable(0, 0)
        info_box.iconphoto(False, ImageTk.PhotoImage(file = "Images/8587213.png"))

        global infoNewImg
        infoImg = Image.open("Images/S (1).png")
        infoResizeImg = infoImg.resize((400, 320)) #Resizing the image
        infoNewImg = ImageTk.PhotoImage(infoResizeImg)
        infoImage1 = Label(info_box, image = infoNewImg, bd = 0)
        infoImage1.place(x = 0, y = 0)

        heading = Label(info_box, text = "Category Description:", font = ("corbel", 21, "bold"), bg = "#FFF6EF")
        heading.place(relx = 0.5, rely = 0.14, anchor = CENTER)

        label_info = Label(info_box, text = explanation, wraplength = 270,
                           font = ("corbel", 15), bg = "#FFF6EF")
        label_info.place(relx = 0.5, rely = 0.44, anchor = CENTER)

        ok_btn = Button(info_box, text = "Ok", width = 10, bg = "#B9DDE5", padx = 2, 
                        font = ("corbel", 14, "bold"), relief = FLAT, command = info_box.destroy)

        ok_btn.place(relx = 0.5, rely = 0.75, anchor = CENTER)

        #Destroying the SelectCategory instance
        self.frame2.destroy()

        #Creating a SelectDifficulty instance
        select_difficulty = SelectDifficulty(self.root, category)


    #Method to retrieve category explanations
    def get_category_explanation(self, category):
        category_explanations = {
            "Entertainment: Japanese Anime and Manga": "This category includes questions about Japanese Anime and Manga",
            "Entertainment: Books": "This category contains questions about books, literature and authors.",
            "Entertainment: Film": "This category contains questions movies and cinema.",
            "Art": "This category includes questions regarding various forms of arts",
            "Celebrities": "This category includes questions about famous personalities",
            "Sports": "This categort contains questions about different kinds of sports all over the world.",
            "General Knowledge": "This category contains questions from various general knowledge topics.",
            "Entertainment: Cartoons and Animations": "This category includes questions about Cartoons and Animations"
        }

        return category_explanations.get(category, "No explanation available for this category.")
    

#-----------------------------------------------------------------------------------# 
#----- Class that represents the difficulty selection screen of the trivia app -----#
#-----------------------------------------------------------------------------------# 
class SelectDifficulty:
    
    def __init__(self, root, category):
        #Initializing the category selection screen and it's layout
        self.root = root
        self.category = category
        self.root.title("Difficulty Selection")
        self.root.geometry("840x580+200+30")

        #Creating a frame within the root window
        self.frame3 = Frame(self.root, width = 840, height = 590)
        self.frame3.pack()

        #Setting a background image
        self.Img = Image.open("Images/Untitled design (4).png")
        self.ResizeImg = self.Img.resize((840, 580)) #Resizing the image
        self.NewImg = ImageTk.PhotoImage(self.ResizeImg)
        self.Image1 = Label(self.frame3, image = self.NewImg, bd = 0)
        self.Image1.place(x = 0, y = 0)

        #Label prompting the user to select difficulty
        self.label3 = Label(self.frame3, text = "Choose Difficulty",
                            font = ("Comic Sans MS", 24, "bold"), bg = "#FFF6EF")
        self.label3.place(relx = 0.5, rely = 0.08, anchor = CENTER)

        self.difficulty_var = StringVar()
        self.difficulty_var.set("easy")

        #Buttons for selecting the difficulty level

        self.easyImg = Image.open("Images/9.png")
        self.easyResizeImg = self.easyImg.resize((160, 55)) #Resizing the image
        self.easyNewImg = ImageTk.PhotoImage(self.easyResizeImg)

        self.easy_btn = Button(self.frame3, text = "Easy", image = self.easyNewImg, bg = "#FFF6EF",
                               font = ("corbel", 15), borderwidth = 0,
                               command = lambda: self.select_difficulty("easy"))
        self.easy_btn.place(relx = 0.5, rely = 0.22, anchor = CENTER)

        self.medImg = Image.open("Images/10.png")
        self.medResizeImg = self.medImg.resize((160, 55)) #Resizing the image
        self.medNewImg = ImageTk.PhotoImage(self.medResizeImg)

        self.medium_btn = Button(self.frame3, text = "Medium", image = self.medNewImg, bg = "#FFF6EF",
                                 font = ("corbel", 15), borderwidth = 0,
                                 command = lambda: self.select_difficulty("medium"))
        self.medium_btn.place(relx = 0.5, rely = 0.34, anchor = CENTER)

        self.hardImg = Image.open("Images/11.png")
        self.hardResizeImg = self.hardImg.resize((160, 55)) #Resizing the image
        self.hardNewImg = ImageTk.PhotoImage(self.hardResizeImg)

        self.hard_btn = Button(self.frame3, text = "Hard", image = self.hardNewImg, 
                               font = ("corbel", 15), borderwidth = 0,
                               command = lambda: self.select_difficulty("hard"))
        self.hard_btn.place(relx = 0.5, rely = 0.46, anchor = CENTER)

        #Label prompting the user to select the time
        self.label4 = Label(self.frame3, text = "Select Time per Question (seconds):",
                            font = ("Comic Sans MS", 18, "bold"), bg = "#FFF6EF")
        self.label4.place(relx = 0.5, rely = 0.6, anchor = CENTER)

        #Variable to store the selected time
        self.time_var = StringVar()
        self.time_var.set("15")
        times = ["No time", "10", "15", "20", "30"]
        self.time_list = OptionMenu(self.frame3, self.time_var, *times)
        self.time_list.config(font = ("arial", 15), width = 11, relief = FLAT,
                              highlightbackground = "#5F3B28", highlightthickness = 3)
        self.time_list.place(relx = 0.5, rely = 0.72, anchor = CENTER)
        # Also increasing the font of the dropdown items
        self.menu = self.frame3.nametowidget(self.time_list.menuname)
        self.menu.config(font = ("arial", 12))

        self.nextImg = Image.open("Images/Untitled design (3).png")
        self.nextResizeImg = self.nextImg.resize((140, 55)) #Resizing the image
        self.nextNewImg = ImageTk.PhotoImage(self.nextResizeImg)

        #Back and Next buttons
        self.next_btn = Button(self.frame3, image = self.nextNewImg, bg = "#FFF6EF", borderwidth = 0,
                               font = ("corbel", 16), command = self.start_quiz)
        self.next_btn.place(relx = 0.5, rely = 0.87, anchor = CENTER)

        self.back_btn = Button(self.frame3, text = "<  Back", borderwidth = 0, bg = "#FFF6EF",
                               font = ("corbel", 17), width = 10, height = 1, command = self.go_back)
        self.back_btn.place(relx = 0.15, rely = 0.08, anchor = CENTER)

    #Method to handle the selection of a difficulty level
    def select_difficulty(self, difficulty):
        self.difficulty_var.set(difficulty)

        #Changing the color of the selected button
        buttons = [self.easy_btn, self.medium_btn, self.hard_btn]
        for button in buttons:
            if button.cget("text").lower() == difficulty:
                button.config(borderwidth = 3, relief=RAISED)
            else:
                button.config(borderwidth = 0)

    #Method to go back to the category selection page
    def go_back(self):
        #Destroying the current frame
        self.frame3.destroy()

        #Creating an instance of category selection screen
        select_category = SelectCategory(self.root)

    #Initializing the quiz logic
    def start_quiz(self):
        self.difficulty = self.difficulty_var.get()
        self.time_per_question = None if self.time_var.get() == "No time" else int(self.time_var.get())
        self.frame3.destroy()
        self.initialize_quiz()

    def initialize_quiz(self):
        #Using the selected category to fetch questions from the API
        category_id = self.get_category_id()

        parameters = {
            #No. of questions per quiz
            "amount": 10,
            #Specifying multiple-choice questions
            "type": "multiple",
            #Using the selected category and difficulty level
            "category": category_id,
            "difficulty": self.difficulty
        }

        #Making an API request to fetch data from the database
        response = requests.get(url = "https://opentdb.com/api.php?amount=10", params = parameters)
        question_data = response.json()["results"]

        #Processing data and creating a list of question objects
        question_bank = []
        for question in question_data:
            quiz_choices = []
            #Using the html module to unescape
            question_text = html.unescape(question["question"])
            correct_answer = html.unescape(question["correct_answer"])
            incorrect_answers = question["incorrect_answers"]

            for ans in incorrect_answers:
                quiz_choices.append(html.unescape(ans))
            quiz_choices.append(correct_answer)
            shuffle(quiz_choices)

            new_question = Quiz_Question(question_text, correct_answer, quiz_choices)
            question_bank.append(new_question)

        #Creating a Quiz_Logic instance
        quiz = Quiz_Logic(question_bank)

        #Creating a Quiz_GUI to display quiz
        ui_quiz = Quiz_GUI(self.root, quiz, self.time_per_question)

    #Method to get the category id of the selected category
    def get_category_id(self):
        #Mapping category names to their respective IDs
        mapping_categories = {
            "Entertainment: Japanese Anime and Manga": 31,
            "Entertainment: Books": 10,
            "Entertainment: Film": 11,
            "Art": 25,
            "Celebrities": 26,
            "Sports": 21,
            "General Knowledge": 9,
            "Entertainment: Cartoons and Animations": 32
        }
        #Setting default to 9(General Knowledge)
        return mapping_categories.get(self.category, 9)


class Quiz_GUI:

    #Contructor method of the Quiz_GUI class
    def __init__(self, root, quiz_logic: Quiz_Logic, time_per_question) -> None:
        #Initializing class attributes
        self.root = root
        self.quiz = quiz_logic
        self.time_per_question = time_per_question
        self.quiz_finish = False
        self.show_result = False

        self.root.title("Trivia App")
        self.root.geometry("840x580+200+30")

        #Setting a background image
        self.Img = Image.open("Images/Easy.png")
        self.ResizeImg = self.Img.resize((840, 580)) #Resizing the image
        self.NewImg = ImageTk.PhotoImage(self.ResizeImg)
        self.Image1 = Label(self.root, image = self.NewImg, bd = 0)
        self.Image1.place(x = 0, y = 0)

        '''Loading sound effects using pygame for correct answer,
           incorrect answer, time's up and game completion.'''
        
        self.correct_sound = pygame.mixer.Sound("Audios/mixkit-game-success-alert-2039.wav")
        self.incorrect_sound = pygame.mixer.Sound("Audios/mixkit-alert-quick-chime-766.wav")
        self.times_up_sound = pygame.mixer.Sound("Audios/mixkit-classic-short-alarm-993.wav")
        self.quiz_complete_sound = pygame.mixer.Sound("Audios/mixkit-game-level-completed-2059.wav")

        #Creating a canvas for displaying the quetion
        
        self.question_text = Label(self.root, text = "Question here", wraplength = 700,
                                   fg = "black", font = ("corbel", 18, "italic"), bg = "#FFF6EF")
        self.question_text.place(relx = 0.5, rely = 0.3, anchor = CENTER)

        #Setting up UI elements and variables for user's answers
        self.answer_by_user = StringVar()
        self.answer_options = self.radio_btns()
        self.response = Label(self.root, pady = 15, font = ("corbel", 17), bg = "#CDCFE9")
        self.response.place(relx = 0.5, rely = 0.77, anchor = CENTER)

        self.nextImg = Image.open("Images/Easy (3).png")
        self.nextResizeImg = self.nextImg.resize((140, 50)) #Resizing the image
        self.nextNewImg = ImageTk.PhotoImage(self.nextResizeImg)

        #Creating a next button for the user during the quiz
        next_btn1 = Button(self.root, text = "Next", image = self.nextNewImg, borderwidth = 0,
                           bg = "#CCCEE9", activebackground = "#CCCEE9",
                           font = ("corbel", 16, "bold"), command = self.next_btn)
        next_btn1.place(relx = 0.5, rely = 0.88, anchor = CENTER)

        #Creating a help button for the user during the quiz
        self.chances_remaining = 2
        self.help_btn = Button(self.root, text = f"Help ({self.chances_remaining} left)", width = 13,
                               bg = "orange", fg = "white", relief = FLAT, activebackground = "#CCCEE9",
                               pady = 3, font = ("corbel", 13, "bold"), command = self.use_help)
        self.help_btn.place(relx = 0.85, rely = 0.87, anchor = CENTER)

        self.pauseImg = Image.open("Images/Easy (4).png")
        self.pauseResizeImg = self.pauseImg.resize((62, 62)) #Resizing the image
        self.pauseNewImg = ImageTk.PhotoImage(self.pauseResizeImg)

        #Button for resuming the quiz
        self.pause_btn = Button(self.root, image = self.pauseNewImg, bg = "#FFF6EF", borderwidth = 0,
                                font = ("corbel", 14, "bold"), command = self.pause_resume_quiz)
        self.pause_btn.place(relx = 0.9, rely = 0.11, anchor = CENTER)

        #Initializing the variables involved in the pausing-resuming functionality
        self.paused = False
        self.pause_screen = None
        self.paused_question = None

        #Setting up labels for displaying the score and timer during the quiz
        self.timer_label = Label(self.root, text = "", font = ("corbel", 17), bg = "#CDCFE9")
        self.timer_label.place(relx = 0.15, rely = 0.85, anchor = CENTER)
        self.timer_seconds = self.time_per_question
        #Tracking whether the timer is already running
        self.timer_running = False
        self.start_timer()

        self.score_label = Label(self.root, text = "Score: 0", font = ("corbel", 17), bg = "#FFF6EF")
        self.score_label.place(relx = 0.12, rely = 0.12, anchor = CENTER)

        '''Using individual functions to display the title, question, options and buttons'''
        self.show_title()
        self.show_question()
        self.show_options()

    #Method to display the title at the top of the window
    def show_title(self):
        title_heading = Label(self.root, text = "Trivia Game", bg = "#FFF6EF",
                              font = ("corbel", 28, "bold"), pady = 6)
        title_heading.place(relx = 0.5, rely = 0.1, anchor = CENTER)

    #Method to display the current question text
    def show_question(self):
        text_Q = self.quiz.successor_question()
        self.question_text.config(text = text_Q) 

    #Method to display the options
    def show_options(self):
        val1 = 0
        self.answer_by_user.set(None)
        for option in self.quiz.present_question.quiz_choices:
            self.answer_options[val1]["text"] = option
            self.answer_options[val1]["value"] = option
            val1 += 1

    #Method to handle the functionality of the next button and evaluating the user's answer
    def next_btn(self):
        #Handling the case when time is up
        if self.timer_seconds == 0:
            self.response["fg"] = "red"
            self.response["text"] = "Time\'s Up!"
            self.times_up_sound.play()
            #Assuming an empty string as the user's answer if the time's up
            self.quiz.answer_checking("")

        #Handling the case when the answer is correct
        elif self.quiz.answer_checking(self.answer_by_user.get()):
            self.response["fg"] = "#475CB6"
            self.response["text"] = "Correct Answer!"
            self.correct_sound.play()
            self.score_update()

        #Handle the case when the answer is incorrect
        else:
            self.response["fg"] = "#B64848"
            self.response["text"] = (f"Wrong!\nThe correct answer was: {self.quiz.present_question.correct_answer}")
            self.incorrect_sound.play()

        #Displaying the next question and resetting the timer
        if self.quiz.if_questions_more():
            self.show_question()
            self.show_options()
            self.reset_timer()
        
        #Displaying the result if no questions are left
        else:
            self.display_result()

    #Method to display the radio buttons
    def radio_btns(self):
        list_of_choices = []
        position_y = 230

        while len(list_of_choices) < 4:
            radio_btn = Radiobutton(self.root, text = "", value = '', font = ("corbel", 16),
                                    variable = self.answer_by_user, bg = "#FFF6EF")
            list_of_choices.append(radio_btn)
            radio_btn.place(x = 120, y = position_y)
            position_y += 40
        return list_of_choices

    #Help button for the user
    def use_help(self):
        if self.chances_remaining > 0:
            options = self.quiz.present_question.quiz_choices
            correct_answer = self.quiz.present_question.correct_answer

            #Making a copy of the options list
            options_copy = options.copy()
            #Removing correct answer from the options copy
            options_copy.remove(correct_answer)
            #Removing one more incorrect answer from the options copy
            #Using random module to select randomly
            incorrect_option = options_copy[random.randint(0, len(options_copy) - 1)]
            options_copy.remove(incorrect_option)

            #Updating the list of options
            for i, option in enumerate(options):
                if option == correct_answer or option == incorrect_option:
                    self.answer_options[i]["text"] = option
                    self.answer_options[i]["value"] = option
                else:
                    self.answer_options[i]["text"] = ""
                    self.answer_options[i]["value"] = ""

            #Decresing chances remaining
            self.chances_remaining -= 1
            #Updating the text on button that shows chances remaining
            self.help_btn["text"] = f"Help ({self.chances_remaining} left)"

            #Disabling the button after two tries
            if self.chances_remaining == 0:
                self.help_btn["state"] = "disabled"
                self.help_btn["bg"] = "#D19852"

    #Method that handles the pause-resume  quiz functionality
    def pause_resume_quiz(self):
        if self.paused:
            self.resume_quiz()
        else:
            self.pause_quiz()

    #Method to pause the quiz and display a pause screen while saving the current state
    def pause_quiz(self):
        self.paused = True
        self.timer_running = False #Stopping the timer

        #Saving the current state of the quiz
        self.paused_question = self.quiz.present_question
        self.paused_score = self.quiz.score
        self.paused_wrong = self.quiz.question_number - self.quiz.right_answers_given

        #Creating a frame inside the main window for displaying the pause screen
        self.pause_screen = Frame(self.root, bg = "white")
        self.pause_screen.place(relwidth = 1, relheight = 1)

        global NewImg
        #Setting a background image
        Img = Image.open("Images/—Pngtree—background.png")
        ResizeImg = Img.resize((840, 580)) #Resizing the image
        NewImg = ImageTk.PhotoImage(ResizeImg)
        Image1 = Label(self.pause_screen, image = NewImg, bd = 0)
        Image1.place(x = 0, y = 0)

        paused_heading = Label(self.pause_screen, text = "Quiz Paused", padx = 12, pady = 6,
                               font = ("corbel", 27, "bold"), bg = "#FFF6EF")
        paused_heading.place(relx = 0.5, rely = 0.25, anchor = CENTER)

        frame1 = Frame(self.pause_screen, bg = "#509BAB", width = 200, height = 52)
        frame1.place(relx = 0.492, rely = 0.411, anchor = CENTER)

        #Displaying a resume button
        resume_btn = Button(self.pause_screen, text = "Resume Quiz", width = 16, pady = 4,
                            font = ("corbel", 16, "bold"), bg = "#A4DAE6", fg = "white", relief = FLAT,
                            command = self.resume_quiz)
        resume_btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)

        frame2 = Frame(self.pause_screen, bg = "#656AAB", width = 200, height = 52)
        frame2.place(relx = 0.492, rely = 0.561, anchor = CENTER)

        #Displaying a leave quiz button
        leave_btn = Button(self.pause_screen, text = "Leave Quiz", width = 16, pady = 4,
                           relief = FLAT, bg = "#ABAFE6", fg = "white",
                           font = ("corbel", 16, "bold"), command = self.leave_quiz)
        leave_btn.place(relx = 0.5, rely = 0.55, anchor = CENTER)

        frame3 = Frame(self.pause_screen, bg = "#D48489", width = 200, height = 52)
        frame3.place(relx = 0.492, rely = 0.711, anchor = CENTER)

        #Displaying a quit application button
        leave_btn = Button(self.pause_screen, text = "Quit Application", width = 16, pady = 4,
                           relief = FLAT, bg = "#F1BFC2", fg = "white",
                           font = ("corbel", 16, "bold"), command = self.root.destroy)
        leave_btn.place(relx = 0.5, rely = 0.7, anchor = CENTER)

    #Method to restore and resume the quiz and updating the GUI
    def resume_quiz(self):
        self.paused = False
        self.timer_running = True #Resuming the timer
        self.pause_screen.destroy()

        #Restoring the saved data
        self.quiz.present_question = self.paused_question
        self.quiz.score = self.paused_score
        self.quiz.right_answers_given = self.quiz.question_number - self.paused_wrong

        #Displaying the elements
        text_Q = f"Q.{self.quiz.question_number}: {self.quiz.present_question.question_text}"
        self.question_text.config(text = text_Q, font = ("corbel", 15, "italic"))

    #Method for the leave quiz button
    def leave_quiz(self):
        #Destroying the current window
        self.root.destroy()

        #Creating a new instance of Tk window
        root = Tk()
        initial_screen = FirstScreen(root)
        root.mainloop()

    #Method to update the score of the player
    def score_update(self):
        self.quiz.score += 1
        self.score_label["text"] = f"Score: {self.quiz.score}/{self.quiz.question_number}"

    #Method to start the timer if it's not running already
    def start_timer(self):
        if not self.timer_running and self.timer_seconds is not None:
            self.timer_running = True
            self.update_timer()

    #Method to update the timer
    def update_timer(self):
        #Stop updating if the window is destroyed
        if not self.root.winfo_exists():
            return
        
        if not self.paused:
            if self.timer_seconds is not None and self.timer_seconds > 0 and not self.quiz_finish:
                #Updating the timer label
                self.timer_label["text"] = f"Time left: {self.timer_seconds}s"
                #Decrementing timer seconds
                self.timer_seconds -= 1
                #Scheduling the next update
                self.root.after(1000, self.update_timer)

            #When timer reaches zero
            elif self.timer_seconds == 0:
                self.timer_label["text"] = ""
                self.timer_running = False
                self.next_btn()

    #Method to reset the timer
    def reset_timer(self):
        if self.timer_seconds is not None:
            self.timer_seconds = self.time_per_question
            self.start_timer()

    #Method for displaying the quiz results
    def display_result(self):
        if self.show_result:
            return #Do nothing if the result has already been displayed
        
        #Setting quiz_finish to True when the quiz is over
        self.quiz_finish = True

        #Calling another method to display results on a Toplevel window
        self.result_window()

        #Indicating that the result has been displayed
        self.show_result = True

        #Scheduling the game complete sound to be played after a short delay
        self.root.after(100, self.quiz_complete_sound.play)

    #Method to create and display a Toplevel window for quiz results
    def result_window(self):
        result_window = Toplevel(self.root)
        result_window.title("Your Quiz Results")
        result_window.geometry("500x470+400+120")
        result_window.resizable(0, 0)
        result_window.iconphoto(False, ImageTk.PhotoImage(file = "Images/8587213.png"))

        global NewImg
        #Setting a background image
        Img = Image.open("Images/S (2).png")
        ResizeImg = Img.resize((500, 470)) #Resizing the image
        NewImg = ImageTk.PhotoImage(ResizeImg)
        Image1 = Label(result_window, image = NewImg, bd = 0)
        Image1.place(x = 0, y = 0)

        #Getting the calculations from the quiz
        correct, wrong, score_percent = self.quiz.calculate_score()

        #Displaying labels accordingly in the Toplevel window
        result_heading = Label(result_window, text = "Quiz Results", font = ("corbel", 23, "bold"), bg = "#FFF6EF")
        result_heading.place(relx = 0.5, rely = 0.08, anchor = CENTER)

        right_answers_label = Label(result_window, text = f"Correct: {correct}", font = ("Georgia", 17), bg = "#FFF6EF")
        right_answers_label.place(relx = 0.5, rely = 0.25, anchor = CENTER)

        wrong_answers_label = Label(result_window, text = f"Wrong: {wrong}", font = ("Georgia", 17), bg = "#FFF6EF")
        wrong_answers_label.place(relx = 0.5, rely = 0.38, anchor = CENTER)

        percent_label = Label(result_window, text = f"Percentage: {score_percent}%", font = ("Georgia", 17), bg = "#FFF6EF")
        percent_label.place(relx = 0.5, rely = 0.51, anchor = CENTER)
 
        global nextNewImg
        nextImg = Image.open("Images/Easy (1).png")
        nextResizeImg = nextImg.resize((150, 48)) #Resizing the image
        nextNewImg = ImageTk.PhotoImage(nextResizeImg)

        #Displaying a play again button
        play_again = Button(result_window, image = nextNewImg, borderwidth = 0,
                            font = ("corbel", 14, "bold"), command = self.leave_quiz)
        play_again.place(relx = 0.5, rely = 0.66, anchor = CENTER)

        global quitNewImg
        quitImg = Image.open("Images/Easy (2).png")
        quitResizeImg = quitImg.resize((150, 48)) #Resizing the image
        quitNewImg = ImageTk.PhotoImage(quitResizeImg)

        #Displaying a quit application button
        quit_btn = Button(result_window, image = quitNewImg, padx = 10, borderwidth = 0,
                          font = ("corbel", 14, "bold"), command = self.root.destroy)
        quit_btn.place(relx = 0.5, rely = 0.8, anchor = CENTER)
    
#Starting the applicating by running the mainloop
if __name__ == "__main__":
    root = Tk()
    initial_screen = FirstScreen(root)
    root.mainloop()