# Quiz Formatting
## File placing
All quizzes are placed at /quizzes in a folder named after the author.
For each quiz, you should provide a JSON-file named after the ID of the quiz.
## Quiz-IDs
The quiz-IDs are incrementing numbers starting at 1. The IDs are counted for each author seperately.
## JSON-format
Each quiz file has a JSON-file representing it.  
Here you see each field listed and what it means.  
* `creator`: **required** The author of the quiz.
* `id`: **required** The quiz-ID. Should be the same as the file name.
* `type`: **required** The type of the question. It can be one of the following:
  * `multipleChoice`: A question with multiple options to answer with.
  * `trueFalse`: A question that can be answered with true or false.
  * `fillInTheBlank`: A question that can be answered with a string (usually a request to fill in a blank).
* `question`: **required** The question to answer.
* `options`: **required for `multipleChoice`** A list of options to answer with.
* `answer`: ***required*** For:
  * `multipleChoice`:  the index of the correct option in the `options`-list
  * `trueFalse`: a boolean that is the correct answer to the question
  * `fillInTheBlank`: a string that is the correct answer to the question
* `difficulty`: ***optional*** A number from 1 to 5, stating how difficult a quiz is to solve. 
  The quiz is ok to answer for:  
  * ``1``: people that just started learning python.
  * ``2``: people that have a few weeks of python experience (4 to 7 weeks).
  * ``3``: every average Python developer.
  * ``4``: more advanced Python users.
  * ``5``: veteran Python hunters.
* `tags`: ***optional*** A list of all tags that apply to the quiz.
Tags defining the features used in a quizes code:
  * `list`: The quiz uses list functions (eg. `map`, `zip`, `reverse` (on a list), `len` (on a list), `insert`, `pop`, etc.) or contains iteration over or modification of a list.
  * `str`: The quiz uses string functions (eg. `isalpha`, `replace`, `reverse` (on a string), `len` (on a string))
  * `dict`: The quiz uses dict functions (eg. `keys`, `reverse` (on a dict), `len` (on a dict), `insert`, `pop`, etc.) or contains iteration over or modification of a dict.
  * `for`: The quiz uses a for loop
  * `while`: The quiz uses a while loop
  * `listcompr`: The quiz uses list comprehension.
  * `dictcompr`: The quiz uses dict comprehension.
  * `eval`: The quiz uses `eval` or `exec`.
  * `inlinestatements`: The quiz uses inline `if`s or `for`s.
  * `func`: The quiz contains func-defs.  
Tags defining what is the topic of the quiz (This needs to be optimized; 'is about' means 'is the "trap" you are supposed to miss of the quiz'):
  * `nameing`: The quiz is about naming specific things.
  * `syntax`: The quiz is about the correct syntax of a specific python feature.
  * `scope`: The quiz is about the scoping of variables.
