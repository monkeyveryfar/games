hidden_word = "waste"
current_guess = " "

def is_correct(word):
  correct = word == hidden_word
  return correct

def generate_hint(word):
  hint = ""
  index = 0
  if hidden_word == current_guess:
    print("Good job, you found the word!")
  while index <=4:
    if hidden_word[index] == word [index]:
       hint = hint + "G"
    else:
      found = False
      for letter in hidden_word:
        if letter == word[index]:
          found = True
      if found:
        hint = hint + "Y"
      else:
        hint = hint + " "
    index = index + 1

  return hint
  
while not is_correct(current_guess):
  current_guess = input()
  print(generate_hint(current_guess))
        