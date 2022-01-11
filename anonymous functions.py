{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "0549c766",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 4\n",
    "b = 3\n",
    "a+b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "8b197f00",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = lambda x, y : x + y\n",
    "s(2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "9d7dbc3c",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "map_iterator = map(lambda s: print(str(s).upper()), 'abc')\n",
    "# print(type(map_iterator))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "fb387a51",
   "metadata": {},
   "outputs": [],
   "source": [
    "# print(list(map_iterator))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "92cc4c97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n",
      "B\n",
      "C\n"
     ]
    }
   ],
   "source": [
    "a = list(map_iterator)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "24b80de5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[None, None, None]\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
