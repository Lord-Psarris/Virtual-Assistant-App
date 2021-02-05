"""to fully understand make sure u go to googles material design site n go over a few things... or everything"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from helpers import main_helper
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel

# for main functionality
import speech_recognition as sr
import wolframalpha
import wikipedia
import requests
import webbrowser
import time
import pyttsx3
import http.client as hype

Window.size = (320, 568)
appId = ''  # get the wolfram alpha app id


class MainApp(MDApp):
    client = wolframalpha.Client(appId)
    speaker = pyttsx3.init()
    voices = speaker.getProperty('voices')  # getting details of current voice
    speaker.setProperty('voice', voices[1].id)
    rate = speaker.getProperty('rate')  # getting details of current speaking rate: 200
    speaker.setProperty('rate', 160)  # setting up new voice rate
    speech = sr.Recognizer()

    # for the app to run
    def build(self):
        self.theme_cls.primary_palette = 'Gray'
        self.theme_cls.theme_style = 'Dark'
        self.connection_check()
        screen = Builder.load_string(main_helper)
        return screen

    def connection_check(self):
        conn = hype.HTTPConnection("www.google.com", timeout=5)
        try:
            conn.request("HEAD", "/")
            conn.close()

        except Exception as e:
            button = MDFlatButton(text='DISMISS', on_release=self.close_)
            self.dialog = MDDialog(text='there is no internet connection',
                                   size_hint=(0.7, 1), buttons=[button])
            self.dialog.open()
            print(f'there is no internet connection: {e}')
            conn.close()

    def close_(self, obj):
        self.dialog.dismiss()

    # for typed search
    def search(self):
        camp = self.search_result()
        self.root.current = 'result'
        self.search_result_label_fill(camp)

    def search_result(self):
        var = self.root.ids.main.ids.search.text
        if var is not '':
            cap = self.non_search(var)
            print(cap)
            return cap
        else:
            pass

    def search_result_label_fill(self, variable):
        label = MDLabel(text='', halign='left', theme_text_color='Custom', text_color=(1, 1, 1, 1),
                        font_style='Caption')
        label.text = variable
        self.root.ids.result.ids.text.add_widget(label)

    # for voice search
    def voice(self):
        print(self.root.current)
        self.root.current = 'voice'

    def voice_search(self):
        try:
            with sr.Microphone() as source:
                print('listening..')
                MainApp.speech.adjust_for_ambient_noise(source)
                audio = MainApp.speech.listen(source)
                co = MainApp.speech.recognize_google(audio)
                print(co)
                if co == 'end':
                    self.root.current = 'main'
                    print('process has been ended')
                else:
                    self.non_search(co)
        except Exception as e:
            print(f'didn\'t catch that, could you come again? {e}')

    def create_left(self, variable=''):
        label = MDLabel(text='', halign='left', theme_text_color='Custom',
                        text_color=(1, 1, 1, 1), font_style='Caption', )
        label.text = variable
        print(label.text)
        self.root.ids.voice.ids.messages.add_widget(label)

    def create_right(self, variable):
        label = MDLabel(text='Hello World', halign='right', theme_text_color='Custom',
                        text_color=(1, 1, 1, 1), font_style='Caption')
        label.text = variable
        self.root.ids.voice.ids.messages.add_widget(label)

    # not used for app building
    def wolfram_search(self, variable):
        res = MainApp.client.query(variable)
        if res['@success'] == 'false':
            print('Question cannot be resolved... you are being redirected to google')
            time.sleep(5)
            webbrowser.open(f'http://google.com/search?q={variable}')  # Go to google.com
        else:
            # pod[0] is the question
            pod0 = res['pod'][0]
            # pod[1] may contain the answer
            pod1 = res['pod'][1]
            if (('definition' in pod1['@title'].lower()) or ('result' in pod1['@title'].lower()) or (
                    pod1.get('@primary', 'false') == 'true')):
                # extracting result from pod1
                result = self.fix_list(pod1['subpod'])
                question = self.fix_list(pod0['subpod'])
                question = self.remove_brackets(question)
                # self.primaryImage(question)
                return result
            else:
                # extracting wolfram question interpretation from pod0
                question = self.fix_list(pod0['subpod'])
                # removing unnecessary parenthesis
                question = self.remove_brackets(question)
                # searching for response from wikipedia
                ret = self.wikipedia_search(question)
                return ret
                # self.primaryImage(question)

    def wikipedia_search(self, variable):
        # running the query
        search_results = wikipedia.search(variable)
        # If there is no result, print no result
        if not search_results:
            print("No result from Wikipedia... you are being redirected to google")
            time.sleep(5)
            webbrowser.open(f'http://google.com/search?q={variable}')  # Go to google.com
        # Search for page... try block
        try:
            page = wikipedia.page(search_results[0])
        except (wikipedia.DisambiguationError, error):
            page = wikipedia.page(error.options[0])

        wiki_title = str(page.title.encode('utf-8'))
        # wiki_summary = str(page.summary.encode('utf-8'))
        # print(wiki_summary)
        wiki_2 = str(page.summary)
        return wiki_2

    def remove_brackets(self, variable):
        return variable.split('(')[0]

    def fix_list(self, variable):
        if isinstance(variable, list):
            return variable[0]['plaintext']
        else:
            return variable['plaintext']

    def play_sound(self, variable):
        MainApp.speaker.say(variable)
        MainApp.speaker.runAndWait()
        MainApp.speaker.stop()

    def primaryImage(self, variable):
        url = 'http://en.wikipedia.org/w/api.php'
        data = {'action': 'query', 'prop': 'pageimages', 'format': 'json', 'piprop': 'original', 'titles': variable}
        try:
            res = requests.get(url, params=data)
            key = res.json()['query']['pages'].keys()
            for i in key:
                keys = i
            if keys == "-1":
                pass
            else:
                imageUrl = res.json()['query']['pages'][keys]['original']['source']
                print(imageUrl)
        except:
            print('there was an exception processing the image')

    def play_n_print(self, variable):
        statement_1 = variable
        print(statement_1)
        self.play_sound(statement_1)

    def non_search(self, variable):
        variable.lower()
        if variable == "what is your name" or variable == "whats your name" or variable == "what's your name":
            return 'My name is Athena, thanks for asking.'
        elif variable == "what would you like to call yourself":
            return 'I would like to be called "The greatest dopest finest virtual beauty there is" but Lord' \
                   ' psarris says its too much'
        elif variable == "when were you created":
            return 'I have no idea. You an ask Lord psarris about that.'
        elif variable == "who is lord sarris":
            return 'Lord is my creator, he\'s a really awesome guy'
        elif variable == "who is jesus":
            return 'Jesus is the Son of God, who died to redeem us from the curse of the law.'
        elif variable == "thank you":
            return 'you are welcome.'
            exit()
        elif variable == "thank you that will be all":
            return 'you are welcome.'
            exit()
        else:
            return self.wolfram_search(variable)


# screens
class VoiceScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class ResultScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(VoiceScreen(name='voice'))
sm.add_widget(ResultScreen(name='result'))

MainApp().run()
