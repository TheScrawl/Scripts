import sys, time
printf = sys.stdout.write
flush = sys.stdout.flush

def sp(text, speed):
    for char in text:
        printf(char)
        time.sleep(speed)
    flush()

sp('''------------------------------------------------------------------     
Hi.
My name is Bit, and if you're hearing this, i'm already dead.
It also means Porthack.Heart's stopped, and my scripts worked.
Which means we're finished.
Which means you've done it.
Doing this now was our last chance I think.
While they're in a rush to finish it all, and not under the eyes of the whole world yet...
So... thanks.
Thanks.
If all's gone right, there's just one copy of Hacknet left to delete 
and you're looking at it.''', 0.06)
