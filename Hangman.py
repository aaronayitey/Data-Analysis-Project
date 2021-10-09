{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5afbc0a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Let's play Hangman!\n",
      "************\n",
      "____________\n",
      "|          |\n",
      "|           \n",
      "|           \n",
      "|           \n"
     ]
    }
   ],
   "source": [
    "print(\"Let's play Hangman!\")\n",
    "print('************')\n",
    "print('____________')\n",
    "print('|          |')\n",
    "print('|           ')\n",
    "print('|           ')\n",
    "print('|           ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a122a972",
   "metadata": {},
   "outputs": [],
   "source": [
    "word = ['python']\n",
    "word_list = []\n",
    "\n",
    "while True:\n",
    "    guess = input('guess a letter in the secret word: ')\n",
    "    for guess in word :\n",
    "        word_list.append(guess)\n",
    "        if guess in word :\n",
    "            print(word)\n",
    "        else:\n",
    "            print('_')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27c8af6c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
