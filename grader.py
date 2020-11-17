import io, sys, unittest
from unittest.mock import patch
from types import ModuleType
from nbformat import read

def get_source(exercise):
    chapter = exercise.split()[1].split('.')[0]
    paths = {'1':'01-intro.ipynb',
             '2':'02-variables.ipynb',
             '3':'03-conditional.ipynb',
             '4':'04-functions.ipynb',
             '5':'05-iterations.ipynb',
             '6':'06-strings.ipynb',
             '7':'07-files.ipynb',
             '8':'08-lists.ipynb',
             '9':'09-dictionaries.ipynb',
             '10':'10-tuples.ipynb'}
    path = paths[chapter]

    # load the notebook object
    with io.open(path, 'r', encoding='utf-8') as f:
        nb = read(f, 4)
    for cell in nb.cells:
        if cell['cell_type'] != 'code':
            continue
        first = cell['source'].split('\n')[0]
        if first == f'exercise = \'{exercise}\'':
            return cell['source']
    return None

def check_exercise(exercise):
    test = 'test_' + exercise.replace(' ','_').replace('.','_').lower()
    suite = unittest.TestSuite()
    suite.addTest(Exercise(test))

    temp_err = io.StringIO()
    runner = unittest.TextTestRunner(stream=temp_err)
    runner.failfast = True
    result = runner.run(suite)
    if len(result.errors) > 0:
        print(temp_err.getvalue(), file=sys.stderr)
    if len(result.failures) > 0:
        print(temp_err.getvalue(), file=sys.stderr)

def truncate(sio):
    sio.truncate(0)
    sio.seek(0)
    return sio

class Exercise(unittest.TestCase):
    def setUp(self):
        self.errors = False
        self.test_module = ModuleType('mymodule')
        sys.modules['mymodule'] = self.test_module
        self.temp_out = io.StringIO()
        self.old_stdout = sys.stdout
        sys.stdout = self.temp_out

    def tearDown(self):
        sys.stdout = self.old_stdout
        if not self.errors:
            print('All tests passed!', file=sys.stdout)
            

    def checkMC(self, exercise, correct):
        try:
            source = get_source(exercise)
            exec(source, self.test_module.__dict__)
            self.assertEqual(self.temp_out.getvalue(),f"{repr(correct)}\n")
        except AssertionError:
            self.errors = True
            print(f"Error: Wrong answer", file=sys.stderr)
            return
        except:
            self.errors = True
            raise

    def checkPrint(self, exercise, exp_output, mock_input=None, exp_input_num=None, input_val=None, error=None, output_type=None):
        try:
            self.temp_out = truncate(self.temp_out)
            source = get_source(exercise)
            exec(source, self.test_module.__dict__)
            if output_type == list or output_type == dict:
                self.assertEqual(eval(self.temp_out.getvalue()),exp_output)
            elif output_type == "dict_set":
                self.assertEqual(set(eval(self.temp_out.getvalue())), exp_output)
            else:
                self.assertEqual(self.temp_out.getvalue(),exp_output)
        except AssertionError:
            if self.errors == False:
                self.errors = True
                if error:
                    print(error, file=sys.stderr)
                else:
                    print(f"Error:    Wrong Value", file=sys.stderr)
                    print(f"Input:    {input_val}", file=sys.stderr)
                    print(f"Expected: {repr(exp_output)}", file=sys.stderr)
                    print(f"Actual:   {repr(self.temp_out.getvalue())}", file=sys.stderr)
        except:
            self.errors = True
            raise

        if mock_input:
            try:
                self.assertEqual(mock_input.call_count, exp_input_num)
            except AssertionError:
                if self.errors == False:
                    self.errors = True
                    print("Error: The input() function was not called", file=sys.stderr)
            except:
                self.errors = True
                raise

    ################################
    ########## Chapter 01 ##########
    ################################
    def test_exercise_1_1(self):
        self.checkMC('Exercise 1.1', 'c')
        
    def test_exercise_1_4(self):
        self.checkMC('Exercise 1.4', 'a')
        
    def test_exercise_1_6(self):
        self.checkMC('Exercise 1.6', 'b')

    def test_exercise_1_7(self):
        self.checkMC('Exercise 1.7', 'b')


    ################################
    ########## Chapter 02 ##########
    ################################
    @patch('builtins.input', side_effect=['Chuck'])
    def test_exercise_2_2(self, mock_input):
        self.checkPrint(exercise='Exercise 2.2',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output="Hello Chuck\n",
                        input_val='Chuck')

    @patch('builtins.input', side_effect=['35', '2.75'])
    def test_exercise_2_3(self, mock_input):
        self.checkPrint(exercise='Exercise 2.3',
                        mock_input=mock_input,
                        exp_input_num=2,
                        exp_output='Pay: 96.25\n',
                        input_val="'35' and '2.75")

    def test_exercise_2_4(self):
        self.checkPrint(exercise='Exercise 2.4',
                        exp_output="8 <class 'int'> 8.5 <class 'float'> 4.0 <class 'float'> 11 <class 'int'>\n",
                        error="At least one of your answers is wrong.")

    @patch('builtins.input', side_effect=['0', '54.9'])
    def test_exercise_2_5(self, mock_input):
        self.checkPrint(exercise='Exercise 2.5',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output="Fahrenheit: 32.0\n",
                        input_val='0')

        self.checkPrint(exercise='Exercise 2.5',
                        mock_input=mock_input,
                        exp_input_num=2,
                        exp_output="Fahrenheit: 130.82\n",
                        input_val='54.9')

    ################################
    ########## Chapter 03 ##########
    ################################
    @patch('builtins.input', side_effect=['35', '2.75','45','10'])
    def test_exercise_3_1(self, mock_input):
        self.checkPrint(exercise='Exercise 3.1',
                        mock_input=mock_input,
                        exp_input_num=2,
                        exp_output="Pay: 96.25\n",
                        input_val="Hours='35' and Rate='2.75'")

        self.checkPrint(exercise='Exercise 3.1',
                        mock_input=mock_input,
                        exp_input_num=4,
                        exp_output="Pay: 475.0\n",
                        input_val="Hours='45' and Rate='10'")

    @patch('builtins.input', side_effect=['35','2.75','45','10','20','nine','forty'])
    def test_exercise_3_2(self, mock_input):
        self.checkPrint(exercise='Exercise 3.2',
                        mock_input=mock_input,
                        exp_input_num=2,
                        exp_output="Pay: 96.25\n",
                        input_val="'35' and '2.75'")

        self.checkPrint(exercise='Exercise 3.2',
                        mock_input=mock_input,
                        exp_input_num=4,
                        exp_output="Pay: 475.0\n",
                        input_val="'45' and '10'")

        self.checkPrint(exercise='Exercise 3.2',
                        mock_input=mock_input,
                        exp_input_num=6,
                        exp_output="Error, please enter numeric input\n",
                        input_val="'20' and 'nine'")

        
        self.checkPrint(exercise='Exercise 3.2',
                        mock_input=mock_input,
                        exp_input_num=7,
                        exp_output="Error, please enter numeric input\n",
                        input_val="'forty'")

    @patch('builtins.input', side_effect=['-1','-0.1','0','0.1','0.55','0.6','0.65','0.7','0.75','0.8','0.85','0.9','0.95','1.00','1','1.1','10','perfect'])
    def test_exercise_3_3(self, mock_input):
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output="Bad score\n",
                        input_val="'-1'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=2,
                        exp_output="Bad score\n",
                        input_val="'-0.1'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=3,
                        exp_output="F\n",
                        input_val="'0'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=4,
                        exp_output="F\n",
                        input_val="'0.1'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=5,
                        exp_output="F\n",
                        input_val="'0.55'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=6,
                        exp_output="D\n",
                        input_val="'0.6'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=7,
                        exp_output="D\n",
                        input_val="'0.65'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=8,
                        exp_output="C\n",
                        input_val="'0.7'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=9,
                        exp_output="C\n",
                        input_val="'0.75'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=10,
                        exp_output="B\n",
                        input_val="'0.8'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=11,
                        exp_output="B\n",
                        input_val="'0.85'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=12,
                        exp_output="A\n",
                        input_val="'0.9'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=13,
                        exp_output="A\n",
                        input_val="'0.95'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=14,
                        exp_output="A\n",
                        input_val="'1.00'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=15,
                        exp_output="A\n",
                        input_val="'1'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=16,
                        exp_output="Bad score\n",
                        input_val="'1.1'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=17,
                        exp_output="Bad score\n",
                        input_val="'10'")
        self.checkPrint(exercise='Exercise 3.3',
                        mock_input=mock_input,
                        exp_input_num=18,
                        exp_output="Bad score\n",
                        input_val="'perfect'")

    ################################
    ########## Chapter 04 ##########
    ################################
    def test_exercise_4_4(self):
        self.checkMC('Exercise 4.4', 'd')

    def test_exercise_4_5(self):
        self.checkMC('Exercise 4.5', 'd')

    @patch('builtins.input', side_effect=['35','2.75','45','10','20','nine','forty'])
    def test_exercise_4_6(self, mock_input):
        self.checkPrint(exercise='Exercise 4.6',
                        mock_input=mock_input,
                        exp_input_num=2,
                        exp_output="Pay: 96.25\n",
                        input_val="'35' and '2.75'")

        self.checkPrint(exercise='Exercise 4.6',
                        mock_input=mock_input,
                        exp_input_num=4,
                        exp_output="Pay: 475.0\n",
                        input_val="'45' and '10'")

        self.checkPrint(exercise='Exercise 4.6',
                        mock_input=mock_input,
                        exp_input_num=6,
                        exp_output="Error, please enter numeric input\n",
                        input_val="'20' and 'nine'")

        
        self.checkPrint(exercise='Exercise 4.6',
                        mock_input=mock_input,
                        exp_input_num=7,
                        exp_output="Error, please enter numeric input\n",
                        input_val="'forty'")

    @patch('builtins.input', side_effect=['-1','-0.1','0','0.1','0.55','0.6','0.65','0.7','0.75','0.8','0.85','0.9','0.95','1.00','1','1.1','10','perfect'])
    def test_exercise_4_7(self, mock_input):
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output="Bad score\n",
                        input_val="'-1'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=2,
                        exp_output="Bad score\n",
                        input_val="'-0.1'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=3,
                        exp_output="F\n",
                        input_val="'0'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=4,
                        exp_output="F\n",
                        input_val="'0.1'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=5,
                        exp_output="F\n",
                        input_val="'0.55'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=6,
                        exp_output="D\n",
                        input_val="'0.6'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=7,
                        exp_output="D\n",
                        input_val="'0.65'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=8,
                        exp_output="C\n",
                        input_val="'0.7'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=9,
                        exp_output="C\n",
                        input_val="'0.75'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=10,
                        exp_output="B\n",
                        input_val="'0.8'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=11,
                        exp_output="B\n",
                        input_val="'0.85'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=12,
                        exp_output="A\n",
                        input_val="'0.9'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=13,
                        exp_output="A\n",
                        input_val="'0.95'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=14,
                        exp_output="A\n",
                        input_val="'1.00'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=15,
                        exp_output="A\n",
                        input_val="'1'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=16,
                        exp_output="Bad score\n",
                        input_val="'1.1'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=17,
                        exp_output="Bad score\n",
                        input_val="'10'")
        self.checkPrint(exercise='Exercise 4.7',
                        mock_input=mock_input,
                        exp_input_num=18,
                        exp_output="Bad score\n",
                        input_val="'perfect'")

    ################################
    ########## Chapter 05 ##########
    ################################

    @patch('builtins.input', side_effect=['4', '5', 'bad data', '7', 'done'])
    def test_exercise_5_1(self, mock_input):
        self.checkPrint(exercise='Exercise 5.1',
                        mock_input=mock_input,
                        exp_input_num=5,
                        exp_output="Invalid input\n16 3 5.333333333333333\n",
                        input_val="'4', '5', 'bad data', '7', and 'done'")

    @patch('builtins.input', side_effect=['4', '5', 'bad data', '7', 'done'])
    def test_exercise_5_2(self, mock_input):
        self.checkPrint(exercise='Exercise 5.2',
                        mock_input=mock_input,
                        exp_input_num=5,
                        exp_output="Invalid input\n4 7\n",
                        input_val="'4', '5', 'bad data', '7', and 'done'")

    ################################
    ########## Chapter 06 ##########
    ################################
    @patch('builtins.input', return_value='Banana')
    def test_exercise_6_1(self, mock_input):
        self.checkPrint(exercise='Exercise 6.1',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output="a\nn\na\nn\na\nB\n",
                        input_val='Banana')

    @patch('builtins.input', side_effect=['Banana','a'])
    def test_exercise_6_3(self, mock_input):
        self.checkPrint(exercise='Exercise 6.3',
                        mock_input=mock_input,
                        exp_input_num=2,
                        exp_output="3\n",
                        input_val="word='Banana', letter='a'")

    def test_exercise_6_4(self):
        self.checkPrint(exercise='Exercise 6.4',
                        exp_output="3",
                        error='Wrong Answer!')

    def test_exercise_6_5(self):
        self.checkPrint(exercise='Exercise 6.5',
                        exp_output="0.8475",
                        error='Wrong Answer!')

    ################################
    ########## Chapter 07 ##########
    ################################
    @patch('builtins.input', side_effect=['mbox-short.txt', 'mbox.txt'])
    def test_exercise_7_1(self, mock_input):
        exp_output = ''
        fhand = open('mbox-short.txt')
        for line in fhand:
            exp_output += (line.rstrip().upper() + '\n')
        fhand.close()

        self.checkPrint(exercise='Exercise 7.1',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output=exp_output,
                        error="Error: Your program isn't working correctly. Make sure you are calling rstrip() and upper() on each of your lines before printing!")

    @patch('builtins.input', side_effect=['mbox-short.txt', 'mbox.txt'])
    def test_exercise_7_2(self, mock_input):
        self.checkPrint(exercise='Exercise 7.2',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output='0.75072\n',
                        input_val='mbox-short.txt')

        self.checkPrint(exercise='Exercise 7.2',
                        mock_input=mock_input,
                        exp_input_num=2,
                        exp_output='0.89413\n',
                        input_val='mbox.txt')


    @patch('builtins.input', side_effect=['mbox.txt', 'missing.tyxt', 'na na boo boo'])
    def test_exercise_7_3(self, mock_input):
        self.checkPrint(exercise='Exercise 7.3',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output='There were 1797 subject lines in mbox.txt\n',
                        input_val='mbox-short.txt')

        self.checkPrint(exercise='Exercise 7.3',
                        mock_input=mock_input,
                        exp_input_num=2,
                        exp_output='File cannot be opened: missing.tyxt\n',
                        input_val='mbox.txt')

        self.checkPrint(exercise='Exercise 7.3',
                        mock_input=mock_input,
                        exp_input_num=3,
                        exp_output="NA NA BOO BOO TO YOU - You have been punk'd!\n",
                        input_val='mbox.txt')

    ################################
    ########## Chapter 08 ##########
    ################################

    @patch('builtins.input', side_effect=['2,8,1,4,9,6,0,3,5,7'])
    def test_exercise_8_1_1(self, mock_input):
        self.checkPrint(exercise='Exercise 8.1.1',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output=[8,1,4,9,6,0,3,5],
                        input_val='2,8,1,4,9,6,0,3,5,7',
                        output_type=list)

    @patch('builtins.input', side_effect=['2,8,1,4,9,6,0,3,5,7'])
    def test_exercise_8_1_2(self, mock_input):
        self.checkPrint(exercise='Exercise 8.1.2',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output=[8,1,4,9,6,0,3,5],
                        input_val='2,8,1,4,9,6,0,3,5,7',
                        output_type=list)

    def test_exercise_8_2_1(self):
        try:
            source = get_source('Exercise 8.2.1')
            exec(source, self.test_module.__dict__)
            print("Edit the file program-fail.txt so that the program fails.", file=sys.stderr)
        except IndexError:
            pass

    def test_exercise_8_2_2(self):
        try:
            source = get_source('Exercise 8.2.2')
            exec(source, self.test_module.__dict__)
        except:
            print("Fix your program so there is no error.", file=sys.stderr)

    @patch('builtins.input', side_effect=['romeo.txt'])
    def test_exercise_8_4(self, mock_input):
        self.checkPrint(exercise='Exercise 8.4',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output=['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder'],
                        input_val='romeo.txt',
                        output_type=list)
        
    @patch('builtins.input', side_effect=['mbox-short.txt'])
    def test_exercise_8_5(self, mock_input):
        self.checkPrint(exercise='Exercise 8.5',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output="stephen.marquard@uct.ac.za\nstephen.marquard@uct.ac.za\nlouis@media.berkeley.edu\nlouis@media.berkeley.edu\nzqian@umich.edu\nzqian@umich.edu\nrjlowe@iupui.edu\nrjlowe@iupui.edu\nzqian@umich.edu\nzqian@umich.edu\nrjlowe@iupui.edu\nrjlowe@iupui.edu\ncwen@iupui.edu\ncwen@iupui.edu\ncwen@iupui.edu\ncwen@iupui.edu\ngsilver@umich.edu\ngsilver@umich.edu\ngsilver@umich.edu\ngsilver@umich.edu\nzqian@umich.edu\nzqian@umich.edu\ngsilver@umich.edu\ngsilver@umich.edu\nwagnermr@iupui.edu\nwagnermr@iupui.edu\nzqian@umich.edu\nzqian@umich.edu\nantranig@caret.cam.ac.uk\nantranig@caret.cam.ac.uk\ngopal.ramasammycook@gmail.com\ngopal.ramasammycook@gmail.com\ndavid.horwitz@uct.ac.za\ndavid.horwitz@uct.ac.za\ndavid.horwitz@uct.ac.za\ndavid.horwitz@uct.ac.za\ndavid.horwitz@uct.ac.za\ndavid.horwitz@uct.ac.za\ndavid.horwitz@uct.ac.za\ndavid.horwitz@uct.ac.za\nstephen.marquard@uct.ac.za\nstephen.marquard@uct.ac.za\nlouis@media.berkeley.edu\nlouis@media.berkeley.edu\nlouis@media.berkeley.edu\nlouis@media.berkeley.edu\nray@media.berkeley.edu\nray@media.berkeley.edu\ncwen@iupui.edu\ncwen@iupui.edu\ncwen@iupui.edu\ncwen@iupui.edu\ncwen@iupui.edu\ncwen@iupui.edu\n",
                        input_val='mbox-short.txt')

    @patch('builtins.input', side_effect=['6','2','9','3','5','done'])
    def test_exercise_8_6(self, mock_input):
        self.checkPrint(exercise='Exercise 8.6',
                        mock_input=mock_input,
                        exp_input_num=6,
                        exp_output="Maximum: 9.0\nMinimum: 2.0\n",
                        input_val="6','2','9','3','5', and'done'")

    ################################
    ########## Chapter 09 ##########
    ################################
    @patch('builtins.input', side_effect=['words.txt'])
    def test_exercise_9_1(self, mock_input):
        self.checkPrint(exercise='Exercise 9.1',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output={'current-day', 'knew', 'programs', 'many', 'essentially', 'ask', 'be', 'analysis', 'these', 'with', 'cell', 'us', 'We', 'would', 'your', 'memory', 'for', 'or', 'write', 'ranging', 'do', 'surrounded', 'like', 'difficult', 'question', 'we', 'could', 'think', 'me', 'solve', 'assistants', 'things', 'The', 'you', 'what', 'in', 'Our', 'someone', 'This', 'computers', 'vasts', 'on', 'speak', 'best', 'humans', 'are', 'solving', 'programming', 'that', 'figure', 'built', '{\\em', 'very', 'language', 'of', 'only', 'will', 'boring', 'helping', 'else', 'care', 'You', 'to', 'laptops', 'if', 'activity', 'living', 'personal', 'needs', 'amounts', 'data', 'creative', 'reasons', 'making', 'know', 'once', 'behalf', 'rewarding', 'often', 'this', 'helpful', 'the', 'from', 'computer', 'take', 'hardware', 'assumes', 'can', 'want', 'phones', 'a', 'fast', 'skills', 'tell', 'have', 'next', 'who', 'kinds', 'out', 'it', 'everyone}', 'program,', 'were', 'If', 'reptitive', 'having', 'problem', 'how', 'daily', 'tasks', 'fun', 'book', 'as', 'Interestingly,', 'continuously', 'Writing', 'newfound', 'is', 'find', 'our', 'explain', 'and', 'mind-numbing', 'lives', 'What', 'program'},
                        input_val='words.txt',
                        output_type="dict_set")

    @patch('builtins.input', side_effect=['mbox-short.txt'])
    def test_exercise_9_2(self, mock_input):
        self.checkPrint(exercise='Exercise 9.2',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output={'Sat': 1, 'Fri': 20, 'Thu': 6},
                        input_val='words.txt',
                        output_type=dict)

    @patch('builtins.input', side_effect=['mbox-short.txt'])
    def test_exercise_9_3(self, mock_input):
        self.checkPrint(exercise='Exercise 9.3',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output={'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,'ray@media.berkeley.edu': 1},
                        input_val='words.txt',
                        output_type=dict)

    @patch('builtins.input', side_effect=['mbox-short.txt', 'mbox.txt'])
    def test_exercise_9_4(self, mock_input):
        self.checkPrint(exercise='Exercise 9.4',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output='cwen@iupui.edu 5',
                        input_val='mbox-short.txt')

        self.checkPrint(exercise='Exercise 9.4',
                        mock_input=mock_input,
                        exp_input_num=2,
                        exp_output='zqian@umich.edu 195',
                        input_val='mbox.txt')

    @patch('builtins.input', side_effect=['mbox-short.txt'])
    def test_exercise_9_5(self, mock_input):
        self.checkPrint(exercise='Exercise 9.5',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output={'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8},
                        input_val='mbox-short.txt',
                        output_type=dict)

    ################################
    ########## Chapter 10 ##########
    ################################

    @patch('builtins.input', side_effect=['mbox-short.txt', 'mbox.txt'])
    def test_exercise_10_1(self, mock_input):
        self.checkPrint(exercise='Exercise 10.1',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output='cwen@iupui.edu 5',
                        input_val='mbox-short.txt')

        self.checkPrint(exercise='Exercise 10.1',
                        mock_input=mock_input,
                        exp_input_num=2,
                        exp_output='zqian@umich.edu 195',
                        input_val='mbox.txt')

    @patch('builtins.input', side_effect=['mbox-short.txt'])
    def test_exercise_10_2(self, mock_input):
        self.checkPrint(exercise='Exercise 10.2',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output='04 3\n06 1\n07 1\n09 2\n10 3\n11 6\n14 1\n15 2\n16 4\n17 2\n18 1\n19 1\n',
                        input_val='mbox-short.txt')
                            
    @patch('builtins.input', side_effect=['mbox-short.txt'])
    def test_exercise_10_3(self, mock_input):
        self.checkPrint(exercise='Exercise 10.3',
                        mock_input=mock_input,
                        exp_input_num=1,
                        exp_output=[('e', 5436), ('a', 5223), ('i', 4494), ('o', 4174), ('r', 4064), ('t', 4050), ('s', 3738), ('u', 3123), ('c', 3088), ('n', 2575), ('p', 2497), ('m', 2436), ('d', 2004), ('l', 1832), ('h', 1392), ('f', 1257), ('k', 1167), ('b', 1134), ('g', 1027), ('v', 997), ('j', 959), ('y', 643), ('w', 586), ('x', 482), ('z', 78), ('q', 57)],
                        input_val='mbox-short.txt',
                        output_type=list)