# DIME Analytics - Data Security Guides - Memorizable strong passwords

Here are some guidelines to create strong passwords that are possible to memorize.
You should use a password manager to create and save
super-strong passwords for all passwords that are not absolutely required to memorize.
Examples of the few passwords you absolutely _must_ memorize are: your computer logon password
and the master password that unlocks your password manager
(where you will store all your other passwords).

## What makes a strong password?

_Skip this section if you're not feeling geeky._

Passwords are often the weakest link in cybersecurity.
Passwords can fail either by being leaked or stolen –
due to bad password handling practices – or by being cracked by hackers.
This guide will not cover the general password practices
that are required for various specific purposes,
but it will help you create a specific type of password:
one that is practically impossible to crack
but which you will still be able to memorize and use without a password management tool.

A password is cracked by someone gaining access to a database
where the "hash" of your password is saved. Read about
[one-way hashes here](https://dimewiki.worldbank.org/wiki/Encryption#One-way_hashing)
and how [hashing is used for passwords here](https://dimewiki.worldbank.org/wiki/Encryption#Example_of_use-case_of_one-way_hashing).
Once someone has access to your
hash, they can start guessing which password led to that hash.
From there they can guess the password very quickly
if it does not have the special features we cover below.

#### Why are special characters required?

Let's say your password uses the letters a-z and is 4 letters long.
That gives us `26^4 = 456,976` possible passwords.
A regular computer can guess about 1 million passwords a second,
so it would take a regular computer 0.46 seconds to guess your password.
If you would also include uppercase letters, digits, and 20 special characters (`#`, `$`, `%`, `&`, etc.)
it would take `((26+26+10+20)^4)/1,000,000 = 45.21` seconds to guess your password.
This only includes passwords exactly of length 4,
but even if we included possible passwords of length 1, 2 and 3 as well it would only go from 45.21 to 45.77 seconds (there aren't very many of those).

Therefore, the of password is much more important than the number of possible characters; but the number of characters still makes a big difference.
To see this, imagine we add one more character and make the password 5 characters.
We now need `(26+26+10+20)^5)/1,000,000 = 3,707` seconds or 1 hour, 1 minute, and 47 seconds to guess the password.
The same calculation if we were to use only lowercase letters is `(26)^5)/1,000,000 = 11.88` seconds.
This is the reason why websites require us to use
lowercase and uppercase letters as well as digits and symbols in our passwords.
But these times are how long it takes to guess all _possible_ passwords,
and so the combination of characters that is _your_ password will probably be found long before all the possible combinations are guessed.

While 1 hour is much slower than 1 second, a smart hacker
– and most of them are very smart –
have already calculated all of these short passwords and saved them on file.
With such a file, the pre-calculated results are cracked instantly with an appropriate algorithm.
A hacker does not even need to have pre-calculated all the possibilities themselves,
since there are hacker websites where these pre-calculated lists are shared.

#### Why are long passwords required?

While we showed that a 4-character password is quickly cracked,
we saw that it was a big jump from 45 seconds with 4 characters to 1 hour with 5 characters.
So the length of passwords is obviously very important.
If we had an 8-character password (a common requirement)
the password would take `(26+26+10+20)^8)/1,000,000 = 2,044,140,858.65` seconds
or 64 years, 299 days, 54 minutes, and 19 seconds to guess all possible combinations.
Again, we are only calculating combinations of exactly 8 characters in length,
but if we were to include all the passwords up to length 8 it would be less than a year more.
Therefore the exponential effect of adding one more character is really the dominant effect.

64 years is certainly a long time,
but we have so far done this calculation assuming only one regular computer guessing passwords.
Hackers have access to home built supercomputers, or have networks of computers
(either their own or computers that they have hacked).
With this arrangement, it is easy to get to a processing power of 1 billion guesses per second,
which means it takes `(26+26+10+20)^8)/1,000,000,000 = 2,044,140.86` seconds or
23 days, 15 hours, 49 minutes, and 1 second to guess an 8-character password.
That is no longer an impossible feat, so we need even longer passwords.

#### The most common shortcut to remembering (and, therefore, cracking) passwords

We have nbow shown that we need to make rather long passwords,
but very few humans can memorize long passwords based on a random sequence of letters.
Instead, we tend to use words in our passwords to make them easier to remember.
Take the password `somegoodtime`. It has a length of 12 characters, so
it would take a network of 1 million regular computers almost 3,000 years to guess all the possible combinations.

However, hackers are – as already stated – very smart, and
they know that humans use words to make passwords easier to remember.
Actually, the words `some`, `good`, and `time`
are all on the list of the 100 most common four-letter words in the English language,
so if a hacker tried different potential combinations from just that list
it would take a regular computer `((100)^3)/1,000,000 = 1` second to guess that password.
While there is no way for the hacker to know that the password is made of exactly three four-letter words,
it only took 1 second to search this common list.
Therefore the hacker can quickly test other combinations of common words.

## Creating a _secure_, memorizable, long password

We have shown above that the most important thing is that a password is long.
15 characters long should be a minimum when it is used to protect confidential data,
or used as a password manager master password.
Long passwords made out of words are easier to remember, but if we use very common words
then the password is still too easy to crack even if it is long.
This section presents our recommended way to create a very secure password that is long and yet not too difficult to memorize.

#### Step 1 of 4: Create a random starting point

We will still use words to create these long and secure passwords.
This is safe as long as we do not use very common words and we mix them up a bit.
We also want to ensure that no one can guess your password by doing research about your history or personality.
For example, _football_ is always among the most common passwords when cyber-experts study password leaks.
So if you are know to love football (or known to hate football for that matter)
you should not include that in your password.
To make sure that you have a random starting point, go to this
[random word generator](https://passwordcreator.org/commonwords.html#great)
to see ten lists of six randomized words.

If you do not mind typing this much,
then the most secure thing you can do is to pick one of these six lists
(or re-load the page to get ten new lists)
and you have an extremely safe password by using all those words in that order.
Just add a symbol, a digit, and/or an uppercase letter at the end of that password
if that is required where you are using it.

If you do not want to type that much each time you use your password,
then you should still pick one of those six word lists as your starting point.
The first thing you want to do after you choose a list is to test type it.
Are there some words that are difficult to type?
Is the finger movement needed on the keyboard awkward?
If so, drop that word from the list.
If you need to drop more than three words,
then you should start over with a new six word list.

#### Step 2 of 4: Drop the most common words

You should now have a list of three to six randomly selected words
that cannot be guessed based on any knowledge of you.
We want to cut this down to a list of three or four words,
but since a list of three or four words is much less secure than a list of six words
we should cut out the most common words. Test all the words still in your list using this
[word frequency tool](https://www.wordandphrase.info/frequencyList.asp).
You can only do 20 look-ups for free,
but you can reset that count by reloading the page in a private or incognito tab.
You should never have a word that is ranked in the top 2,500 most common.
Drop any such words and then the most common until you are down to three or four words. (To get the rank you need to test the "base form" of the word, e.g. use _index_ instead of _indices_, and _affix_ instead of _affixed_).

Consider dropping any word that has a rank of 5,000 or less.
If you want to keep it, make note of that word, and you must mix it up in the last step.
In the end we want to have three or four words.
If you drop so many words you have less than that, you can add words in next step.
Make sure that, in the end, at least one of the words in your list has a rank above or close to 10,000.
You can always start over with a new random list of six words.

Make sure that your rarest word is not a combination of two common words.
For example, the word _minnow_ is uncommon,
but it is composed of the two common words _min_ and _now_
making the word _minnow_ easy to crack anyways.
Minnow does not have any etymological relation to min or now,
but that is irrelevant here.

#### Step 3 of 4: Add a rare word of your own

In this section you should fill up your list so that you are back at a list of 4 words.
If you already have a list of 4 words you should replace one or two of them in this section.
Here are some ways you can pick a word of your own:

* Most tools to crack passwords only focus on the English language.
So if you speak another language, go back to the random word generator,
pick one word that is not too common,
translate that word to your other language, and use the translated word (be careful to avoid non-English characters as these can cause problems in some cases).
* If you do not speak another language, you can randomize a word in a different language.
The random word generator we used in the first step has multiple languages.
Use an uncommon language, like Dutch. Pick a
[Dutch word here](https://passwordcreator.org/nl.html).
Make sure it is not spelled just like any word in English and
make sure that the word does not mean something very common like `some` or `time`.
Make also sure it is a word that you can memorize and spell.
* Another thing you can do if you do not speak another language
is to pick a foreign place name that you know of
but is unlikely to show up in a hacker's word list (not a popular destination: Paris, Miami, Tokyo, and so on are definitely in there).
This should be a short name and a word that does not mean anything in English.
Do not make it too easy to guess it by doing research on you,
like the town you or your parents were born in,
but use the name of a small town you went on vacation to that you remember.
However, do not use it if everyone around you knows it was your favorite vacation destination.

#### Step 4 of 4: Mix it up a bit

Your four-word list should now be quite easy to memorize, and
since we have avoided too-common words, it is very difficult to crack.
In this final step we will go from difficult to crack to practically impossible to crack.
So far we have only been using lower case letters.
As we shown before, length is more important than the characters you use and, by using words,
we have created a very long password.
However, the only weakness to using words is that it provides a short-cut to hackers.
By using special symbols intelligently we will make that shortcut practically unusable.

By in-fixing a symbol into a word, for example `melod;ic`
we have made the word `melodic` much more difficult to match towards a word list
without making it too much more difficult to remember.
Try to use digits, `,`,`.`,`/`,`;`,`'`,`[`,`]`,
or other non-letter-characters that you can type without using the shift button.
That tends to make it easier to type the password without errors.
In other languages, keyboards have different layouts and different symbols are "shiftless".
Additionally, do not use `3` to replace an `e`, like in `lov3`, or `0` for `o`, like in `s0me`.
While you won't find `lov3` and `s0me` in the word frequency tool above,
you can be sure that hackers have such words included in their word lists.

Finally, make sure that your password is at least 15 characters long.
If that is the case, you have created an insanely secure password that you should be able to remember.
Write down a few clues for yourself, for example
"_; after d in m-word_" to remember anything you did to mix up the words you are using, e.g. `melod;ic`.
Once you know that you have memorized the password you should delete or throw away such clues.
Spaces don't really matter: from a cracking perspective it does not make a big difference if your password is
`covet tighter nets stone` or `covettighternetsstone`,
but the latter tends to be more difficult for someone to try to read over your shoulder as you type it.

Happy impossible-to-crack-password creating!
