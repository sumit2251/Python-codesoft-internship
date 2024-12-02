{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d06913ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "\n",
    "def add_task():\n",
    "    task = task_entry.get()\n",
    "    if task:\n",
    "        task_listbox.insert(tk.END, task)\n",
    "        task_entry.delete(0, tk.END)\n",
    "\n",
    "def remove_task():\n",
    "    selected_task_index = task_listbox.curselection()\n",
    "    if selected_task_index:\n",
    "        task_listbox.delete(selected_task_index)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6432b2a",
   "metadata": {},
   "source": [
    "### Create the main window"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "187ceb2d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "root = tk.Tk()\n",
    "root.title(\"To-Do List\")\n",
    "root.geometry(\"400x650+400+100\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4406cea8",
   "metadata": {},
   "source": [
    "### Create a listbox to display tasks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "25e768d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "task_listbox = tk.Listbox(root)\n",
    "task_listbox.pack(pady=10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76d74fe4",
   "metadata": {},
   "source": [
    "### Create an entry widget to add new tasks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8f55c4ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "task_entry = tk.Entry(root)\n",
    "task_entry.pack(pady=10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f4fa317a",
   "metadata": {},
   "source": [
    "### Create Add and Remove buttons"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "62cf55cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "add_button = tk.Button(root, text=\"Add Task\", command=add_task)\n",
    "remove_button = tk.Button(root, text=\"Remove Task\", command=remove_task)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c0cbaecf",
   "metadata": {},
   "outputs": [],
   "source": [
    "add_button.pack()\n",
    "remove_button.pack()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ceaae381",
   "metadata": {},
   "source": [
    "### Start the Tkinter main loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "768cdd2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "442ba6db",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}