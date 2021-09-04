import time

import discord
import os
import random

client = discord.Client()
x = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith('!graph'):
        global x
        x = 0
        equation = reformat(message.content, '!graph')
        values = loop(equation)
        text1 = ''
        for i in range(10):
            text = '.'
            for j in range(10):
                if values[j] != (9 - i) + 1:
                    text = text + '⬜'
                else:
                    text = text + '⬛'
            # await message.channel.send(text)
            text1 = text1 + text + '\n'
        await message.channel.send(text1)
        await message.channel.send('.:zero::one::two::three::four::five::six::seven::eight::nine:')
        # answer = solve(equation)[0]
        # print(answer)
        # await message.channel.send(answer)

    if message.content.startswith('!test'):
        for i in range(10):
            time.sleep(0.2)
            await message.channel.send('⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜.')


def reformat(text, key):
    return text.replace(key, '').replace(' ', '').replace('y=', '')


async def output(values, message):
    pass


def loop(equation):
    global x
    columns = 10
    arr = [0] * columns
    for i in range(columns):
        x = x + 1
        arr[i] = solve(equation)[0]
    return arr


def solve(equation):
    eq_arr = list(equation)
    if find_arr(eq_arr, '+') != -1:
        pos = find_arr(eq_arr, '+')
        # print(convert(extract_nums_before(eq_arr, pos)))
        # print(convert(extract_nums_after(eq_arr, pos)))
        ans = int(convert(extract_nums_before(eq_arr, pos))) + int(convert(extract_nums_after(eq_arr, pos)))
        # print(eq_arr)
        new_arr = del_range(eq_arr, pos - nums_before(eq_arr, pos), pos + nums_after(eq_arr, pos))
        new_arr.insert(pos - nums_before(eq_arr, pos), ans)
    return new_arr


def extract_nums_before(a, pos):
    arr = list(a)
    i = 0
    if ord(arr[pos - 1]) == 120:
        return list(str(x))
    while True:
        if (pos - i - 1 != -1) & is_a_num(arr[pos - i - 1]):
            i = i + 1
        else:
            break
    arr = del_range(arr, pos, len(arr) - 1)
    arr = del_range(arr, 0, pos - i)
    return arr


def nums_before(a, pos):
    arr = list(a)
    i = 0
    if ord(arr[pos - 1]) == 120:
        return 1
    while True:
        if (pos - i - 1 != -1) & is_a_num(arr[pos - i - 1]):
            i = i + 1
        else:
            break
    return i


def extract_nums_after(a, pos):
    arr = list(a)
    i = 0
    if ord(arr[pos + 1]) == 120:
        return list(str(x))
    while True:
        if (pos + i != len(arr) - 1) & is_a_num(arr[pos + i]):
            i = i + 1
        else:
            break
    arr = del_range(arr, pos + i, len(arr) - 1)
    arr = del_range(arr, 0, pos)
    return arr


def nums_after(a, pos):
    arr = list(a)
    i = 0
    if ord(arr[pos + 1]) == 120:
        return 1
    while True:
        if (pos + i != len(arr) - 1) & is_a_num(arr[pos + i]):
            i = i + 1
        else:
            break
    return i


def is_a_num(ch):
    num = ord(ch)
    return num >= 48 & num <= 57


def find_arr(arr, ch):
    if arr is None:
        return -1
    for i in range(len(arr)):
        if arr[i] == ch:
            return i
    return -1


def to_int(ch):
    return ord(ch) - 48


def del_range(a, start, end):
    arr = list(a)
    if start < end:
        for i in range(end - start + 1):
            arr.pop(start)
    elif start > end:
        for i in range(start - end + 1):
            arr.pop(start)
    return arr


def to_string(arr):
    new_str = ''
    for i in range(len(arr)):
        new_str = new_str + str(arr[i])
    return new_str


def convert(s):
    # initialization of string to ""
    new = ""
    if ord(s[0]) == 120:
        return x
    # traverse in the string
    for i in s:
        new += i

        # return string
    return new


client.run('') #add discord bot token here
