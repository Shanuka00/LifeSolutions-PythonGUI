from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time

home = Tk()
home.title("Life Solutions")
home.config(bg="#C0C0C0")

def gen():

    try:
        welcome = "Hi "+entfn.get()+", these are your future problems"
    except:
        messagebox._show('Name error','Please check your first name')
        
    try:
        age = int(time.localtime()[0]) - int(cmbyr.get())
    except:
        messagebox._show('Birth error','Please check your birth details')
        
    gender = int(gend.get())
    if (gender==1 or gender==2):
        pass
    else:
        messagebox._show('Gender error','Please check your gender details')
        
    hymeneal = int(marry.get())
    if (hymeneal==1 or hymeneal==2):
        pass
    else:
        messagebox._show('Marital error','Please check your marital details')

    # Between 15 and 20 age group
    if age >= 16 and age <= 20:

            if gender == 1:
                if hymeneal == 1:
                    messagebox._show(welcome, \
                                     "* අධ්‍යාපන කටයුතු සිදුකර අවසන්ද?\
                                     \n\n* අඩු වයසින් විවාහ වීම නිසා ඇතිවන ගැටලු පිලිබඳව දැනුවත්ද?\
                                     \n* උපත් පාලනය සම්බන්ධ කරුණු දැනුවත්ද?\
                                     \n\n* මිතුරන් නිසා ඇතිවන ගැටලු නිරාකරණය කරගන්නේ කෙසේද?\
                                     \n* ස්ථීර රැකියාවක් සිදුකරන්නේද?\
                                     \n\n* නැන්දා/මාමා කරදර කරනවාද?\
                                     \n\n* දෙමාපියන්ට යුතුකම් ඉටුකිරීමට හැකිද?\
                                     \n\n* ඔබගේ ඉංග්‍රීසි දැනුම් මට්ටම කෙලෙසක පවතීද?")

                elif hymeneal == 2:
                    messagebox._show(welcome, \
                                     "* අධ්‍යාපන කටයුතු සාර්ථකව කරගැනීමට හැකිවේද?\
                                     \n* මුහුණ දීමට නියමිත විභාග වලට ඔබගේ සූදානම කෙබඳුද?\
                                     \n* ඔබ ඔබේ පෙනුම ගැන සැලකිලිමත්ද?\
                                     \n\n* පෙම්වතියක් සිටීද? සිටීනම් ඇයව කන්ට්‍රෝල් කරගත හැකිද?\
                                     \n* තවමත් පෙම්වතියක් නැතිනම් දැන් හොයාගන්ට වෙයි නේද?\
                                     \n* මිතුරන් නිසා ඇතිවන ගැටලු නිරාකරණය කරගන්නේ කෙසේද?\
                                     \n* ඉංග්‍රීසි දැනුම වැඩිකරගැනීමට උනන්දුවක් දක්වන්නේද?\
                                     \n* විනෝදාංශ වල යෙදීමට කාලයක් ඉතිරිද?")

            elif gender == 2:
                if hymeneal == 1:
                    messagebox._show(welcome, \
                                     "* අධ්‍යාපන කටයුතු සිදුකර අවසන්ද?\
                                     \n\n* අඩු වයසින් විවාහ වීම නිසා ඇතිවන ගැටලු පිලිබඳව දැනුවත්ද?\
                                     \n* උපත් පාලනය සම්බන්ධ කරුණු දැනුවත්ද?\
                                     \n\n* මිතුරියන් නිසා ඇතිවන ගැටලු නිරාකරණය කරගන්නේ කෙසේද?\
                                     \n* දැනට රැකියාවක් සිදුකරන්නේද?\
                                     \n\n* නැන්දා/මාමා කරදර කරනවාද?\
                                     \n\n* දෙමාපියන්ට යුතුකම් ඉටුකිරීමට හැකිද?\
                                     \n\n* ඔබගේ ඉංග්‍රීසි දැනුම් මට්ටම කෙලෙසක පවතීද?")

                elif hymeneal == 2:
                    messagebox._show(welcome, \
                                     "* අධ්‍යාපන කටයුතු සාර්ථකව කරගැනීමට හැකිවේද?\
                                     \n* මුහුණ දීමට නියමිත විභාග වලට ඔබගේ සූදානම කෙබඳුද?\
                                     \n* ඔබ ඔබේ පෙනුම ගැන සැලකිලිමත්ද?\
                                     \n\n* පෙම්වතෙක් සිටීද? සිටීනම් ඔහු ඔබට ගැලපේද?\
                                     \n\n* තවමත් පෙම්වතෙක් නැතිනම් දැන් හොයාගන්ට වෙයි නේද?\
                                     \n* මිතුරියන් නිසා ඇතිවන ගැටලු නිරාකරණය කරගන්නේ කෙසේද?\
                                     \n* ඉංග්‍රීසි දැනුම වැඩිකරගැනීමට උනන්දුවක් දක්වන්නේද?\
                                     \n* විනෝදාංශ වල යෙදීමට කාලයක් ඉතිරිද?")

    # Between 21 and 25 age group
    if age >= 21 and age <= 25:

        if gender == 1:
            if hymeneal == 1:
                messagebox._show(welcome, \
                                 "* ඔබේ රැකියා ස්ථානයේ ප්‍රශ්නයක්ද?\
                                 \n\n* බිරිඳ ඔබට කරදර කරන්නේද?\
                                 \n\n* උපත් පාලනය සම්බන්ධයෙන් ගැටලු පවතීද?\
                                 \n\n* මිතුරන් නිසා ඇතිවන ගැටලු නිරාකරණය කරගන්නේ කෙසේද?\
                                 \n* දරුවන් සිටීද? එසේනම් ඔවුන්ගේ ප්‍රශ්න කොහොමද?\
                                 \n* නැන්දා/මාමා කරදර කරනවාද?\
                                 \n\n* දෙමාපියන්ට යුතුකම් ඉටුකිරීමට හැකිද?\
                                 \n\n* ඔබගේ ඉංග්‍රීසි දැනුම් මට්ටම කෙලෙසක පවතීද?")

            elif hymeneal == 2:
                messagebox._show(welcome, \
                                 "* ඔබගේ රැකියාව ස්ථීරද?\
                                 \n\n* පෙම්වතිය ඔබට ප්‍රශ්න නගනවාද?\
                                 \n\n* ඔබ ඔබේ පෙනුම ගැන සැලකිලිමත්ද?\
                                 \n\n* පෙම්වතිය කොතරම් දුරට සාර්ථකද?\
                                 \n\n* ඔබගේ ඉංග්‍රීසි දැනුම් මට්ටම කෙලෙසක පවතීද?\
                                 \n\n* මිතුරන් නිසා ඇතිවන ගැටලු නිරාකරණය කරගන්නේ කෙසේද?\
                                 \n\n* දෙමව්පියන් ඔබට විවාහයකට බල කරයිද?\
                                 \n\n* විනෝදාංශ වල යෙදීමට කාලය ඉතිරිද?")

        elif gender == 2:
            if hymeneal == 1:
                messagebox._show(welcome, \
                                 "* ඔබේ රැකියා ස්ථානයේ ප්‍රශ්නයක්ද?\
                                 \n\n* ස්වාමි පුරුෂයා ඔබට කරදර කරන්නේද?\
                                 \n\n* උපත් පාලනය සම්බන්ධයෙන් ගැටලු පවතීද?\
                                 \n\n* මිතුරියන් නිසා ඇතිවන ගැටලු නිරාකරණය කරගන්නේ කෙසේද?\
                                 \n* දරුවන් සිටීද? එසේනම් ඔවුන්ගේ ප්‍රශ්න කොහොමද?\
                                 \n* ස්වාමියාගේ මව කරදර කරනවාද?\
                                 \n\n* දෙමාපියන්ට යුතුකම් ඉටුකිරීමට හැකිද?\
                                 \n\n* ඔබගේ ඉංග්‍රීසි දැනුම් මට්ටම කෙලෙසක පවතීද?")

            elif hymeneal == 2:
                messagebox._show(welcome, \
                                 "* ඔබගේ රැකියාව ස්ථීරද?\
                                 \n\n* පෙම්වතා ඔබට ප්‍රශ්න නගනවාද?\
                                 \n\n* ඔබ ඔබේ පෙනුම ගැන සැලකිලිමත්ද?\
                                 \n\n* පෙම්වතා කොතරම් දුරට සාර්ථකද?\
                                 \n\n* ඔබගේ ඉංග්‍රීසි දැනුම් මට්ටම කෙලෙසක පවතීද?\
                                 \n\n* මිතුරියන් නිසා ඇතිවන ගැටලු නිරාකරණය කරගන්නේ කෙසේද?\
                                 \n\n* දෙමව්පියන් ඔබට විවාහයකට බල කරයිද?\
                                 \n\n* විනෝදාංශ වල යෙදීමට කාලය ඉතිරිද?")

    # Between 26 and 30 age group
    elif age >= 26 and age <= 30:

        if gender == 1:
            if hymeneal == 1:
                messagebox._show(welcome, \
                                 "* ඔබගේ රැකියා ස්ථානයේ ප්‍රශ්නයක් තිබේද?\
                                 \n\n* බිරිඳගෙන් ඔබට බොහෝසෙයින් කරදරයිද?\
                                 \n\n* ඔබගේ මිතුරන් දැන් කොපමණ දුරට සාර්ථකයිද?\
                                 \n\n* මිතුරන්ගේ බිරින්ඳෑවරුන් සම්බන්ධව ඔබට ප්‍රශ්නයක්ද?\
                                 \n\n* ඔබගේ පෙනුම ගැන තවදුරත් සැලකිලිමත්ද?\
                                 \n\n* ඔබගේ මව හා බිරිඳ අතර ප්‍රශ්න පැනනගීද?\
                                 \n\n* දරු උපත් සම්බන්ධව කලින් සිතා කටයුතු කරන්නේද?\
                                 \n\n* තවමත් ඔබේ ඉංග්‍රීසි දැනුම වැඩිදියුණු වී නැද්ද?")

            elif hymeneal == 2:
                messagebox._show(welcome, \
                                 "* ඔබගේ රැකියා ස්ථානයේ ප්‍රශ්නයක් තිබේද?\
                                 \n\n* පෙම්වතිය විවාහයට බල කරයිද?\
                                 \n\n* ඔබ ඔබේ පෙනුම ගැන සැලකිලිමත්ද?\
                                 \n\n* ඔබගේ මිතුරන් දැන් කොතරම් දුරට සාර්ථකද?\
                                 \n\n* ඔබගේ ඉංග්‍රීසි දැනුම් මට්ටම කෙලෙසක පවතීද?\
                                 \n\n* විවාහක මිතුරන් අසන ගැටලු නිරාකරණය කරන්නේ කෙසේද?\
                                 \n\n* දෙමව්පියන් ඔබට විවාහයකට බල කරයිද?\
                                 \n\n* සහෝදර සහෝදරයින්ගේ විවාහ කටයිතු සිදුවී හමාරද?")

        elif gender == 2:
            if hymeneal == 1:
                messagebox._show(welcome, \
                                 "* ඔබගේ රැකියා ස්ථානයේ ප්‍රශ්නයක් තිබේද?\
                                 \n\n* ස්වාමිපුරුෂයාගෙන් ඔබට බොහෝසෙයින් කරදරයිද?\
                                 \n\n* ඔබගේ මිතුරියන් දැන් කොපමණ දුරට සාර්ථකයිද?\
                                 \n\n* මිතුරියන්ගේ ස්වාමිපුරුෂයන් සම්බන්ධව ඔබට ප්‍රශ්නයක්ද?\
                                 \n\n* ඔබගේ පෙනුම ගැන තවදුරත් සැලකිලිමත්ද?\
                                 \n\n* ඔබ හා ස්වාමියාගේ මව අතර ප්‍රශ්න පැනනගීද?\
                                 \n\n* දරු උපත් සම්බන්ධව කලින් සිතා කටයුතු කරන්නේද?\
                                 \n\n* නෑදෑයින්ගෙන් ඇතිවන ප්‍රශ්න වලට පිලියම් තිබේද?\
                                 \n\n* තවමත් ඔබේ ඉංග්‍රීසි දැනුම වැඩිදියුණු වී නැද්ද?")

            elif hymeneal == 2:
                messagebox._show(welcome, \
                                 "* ඔබගේ රැකියා ස්ථානයේ ප්‍රශ්නයක් තිබේද?\
                                 \n\n* පෙම්වතා විවාහයට බල කරයිද?\
                                 \n\n* ඔබ ඔබේ පෙනුම ගැන සැලකිලිමත්ද?\
                                 \n\n* ඔබගේ මිතුරියන් දැන් කොතරම් දුරට සාර්ථකද?\
                                 \n\n* ඔබගේ ඉංග්‍රීසි දැනුම් මට්ටම කෙලෙසක පවතීද?\
                                 \n\n* විවාහක මිතුරියන් අසන ගැටලු නිරාකරණය කරන්නේ කෙසේද?\
                                 \n\n* දෙමව්පියන් ඔබට විවාහයකට බල කරයිද?\
                                 \n\n* ඔබගේ විනෝදාංශ කටයුතු නිසිපරිදි කරගැනීමට නොහැකිව පසුතැවිල්ලෙන්ද?")

    # Between 31 and 35 age group
    elif age >= 31 and age <= 35:

        if gender == 1:
            if hymeneal == 1:
                messagebox._show(welcome, \
                                 "* රැකියා ස්ථානයේ තවදුරටත් ප්‍රශ්න පැන නගීද?\
                                 \n\n* බිරිඳගෙන් ඇතිවන කරදර වල අඩුවක් නැද්ද?\
                                 \n\n* උපත් පාලනයේදී ගැටලු ඇතිවේද?\
                                 \n\n* දරුවන් අධ්‍යාපන කටයුතු වලට සූදානම් කල හැකිද?\
                                 \n\n* නැන්දා/මාමා තවමත් ඔබට හිසරදයක්ද?\
                                 \n\n* දරුවන්ගේ සෞඛ්‍ය පිලිබඳව සැලකිලිමත්ද?\
                                 \n\n* දෙමාපියන්ගේ සෞඛ්‍ය පිලිබඳව සැලකිලිමත්ද?\
                                 \n\n* මිතුරන් හා පවතින සබඳතා දුරස් වීද?")

            elif hymeneal == 2:
                messagebox._show(welcome, \
                                 "* රැකියාව තවමත් ස්ථීර කරගැනීමට නොහැකි වූයේද?\
                                 \n\n* තවමත් පෙම්වතියක් සොයාගැනීමට නොහැකි වීද?\
                                 \n\n* පෙම්වතියක් සිටීනම් ඇය විවාහයකට බල කරයිද?\
                                 \n\n* පෙම්වතිය කොතරම් දුරට සාර්ථකද?\
                                 \n\n* දෙමව්පියන් සම්බන්ධව ප්‍රශ්න පවතීද?\
                                 \n\n* තවමත් විනෝදාංශ කටයුතු වල නියැලෙන්නේද?\
                                 \n\n* ඉංග්‍රීසි භාෂා දැනුම කොතරම් දුරකට වර්ධනය කරගෙන සිටීද?")

        elif gender == 2:
            if hymeneal == 1:
                messagebox._show(welcome, \
                                 "* රැකියා ස්ථානයේ තවදුරටත් ප්‍රශ්න පැන නගීද?\
                                 \n\n* ස්වාමියාගෙන් ඇතිවන කරදර වල අඩුවක් නැද්ද?\
                                 \n\n* උපත් පාලනයේදී ගැටලු ඇතිවේද?\
                                 \n\n* දරුවන් අධ්‍යාපන කටයුතු වලට සූදානම් කල හැකිද?\
                                 \n\n* ස්වාමියාගේ මව තවමත් ඔබට හිසරදයක්ද?\
                                 \n\n* දරුවන්ගේ සෞඛ්‍ය පිලිබඳව සැලකිලිමත්ද?\
                                 \n\n* ගෙදර දොර ප්‍රශ්න වලට තනිවම පිලියම් සෙවිය හැකිද?\
                                 \n\n* මිතුරන් හා පවතින සබඳතා දුරස් වීද?")

            elif hymeneal == 2:
                messagebox._show(welcome, \
                                 "* රැකියාව තවමත් ස්ථීර කරගැනීමට නොහැකි වූයේද?\
                                 \n\n* තවමත් පෙම්වතෙකු සොයාගැනීමට නොහැකි වීද?\
                                 \n\n* පෙම්වතෙක් සිටීනම් ඔහු විවාහයකට බල කරයිද?\
                                 \n\n* පෙම්වතා කොතරම් දුරට සාර්ථකද?\
                                 \n\n* දෙමව්පියන් සම්බන්ධව ප්‍රශ්න පවතීද?\
                                 \n\n* තවමත් විනෝදාංශ කටයුතු වල නියැලෙන්නේද?\
                                 \n\n* ඉංග්‍රීසි භාෂා දැනුම කොතරම් දුරකට වර්ධනය කරගෙන සිටීද?")

    # Between 36 and 40 age group
    elif age >= 36 and age <= 40:

        if gender == 1:
            if hymeneal == 1:
                messagebox._show(welcome, \
                                 "* රැකියා ස්ථානයේ ගැටලු වලට සාර්ථක පිලියම් යෙදිය හැකිද?\
                                 \n\n* තම බිරිඳ එපාවීමකට ලක්වීද?\
                                 \n\n* උපත් පාලන කටයුතු නිසියාකාරව කරගන්නේද?\
                                 \n\n* පැරණි මිතුරන් හා පැවති සබඳතා නැතිවීමේ අවධානමක් තිබේද?\
                                 \n\n* නැන්දා/මාමා අසනීප වූ විට බෙහෙත් ගැනීමට සල්ලි තිබේද?\
                                 \n\n* දෙමව්පියන්ගේ සෞඛ්‍ය තත්ත්වයන් පිලිබඳව සැලකිලිමත්ද?\
                                 \n\n* දරුවන්ගේ අධ්‍යාපන කටයුතු නිසියාකාරව සිදුවේද?")

            elif hymeneal == 2:
                messagebox._show(welcome, \
                                 "* රැකියා ස්ථානයේ ගැටලු වලට සාර්ථක පිලියම් යෙදිය හැකිද?\
                                 \n\n* පෙම්වතිය සම්බන්ධව ගැටලු පවතීද?\
                                 \n\n* තම පෙනුම ගැන සැලකිලිමත් වීමට කාලයක් ඉතිරිද?\
                                 \n\n* පෙම්වතිය කොතරම් දුරට සාර්ථකද?\
                                 \n\n* විවාහයක් සිදුකරගැනීමට අවශ්‍ය ආර්ථික ශක්තිය පවතීද?\
                                 \n\n* දෙමව්පියන්ගේ සෞඛ්‍ය තත්ත්වයන් පිලිබඳව සැලකිලිමත්ද?\
                                 \n\n* ඔබගේ මිතුරන් ගතකරන ජීවිතය කෙබඳුද?")

        elif gender == 2:
            if hymeneal == 1:
                messagebox._show(welcome, \
                                 "* රැකියා ස්ථානයේ ගැටලු වලට සාර්ථක පිලියම් යෙදිය හැකිද?\
                                 \n\n* තම සැමියා එපාවීමකට ලක්වීද?\
                                 \n\n* උපත් පාලන කටයුතු නිසියාකාරව කරගන්නේද?\
                                 \n\n* මිතුරියන් හා පැවති සබඳතා නැතිවීමේ අවධානමක් තිබේද?\
                                 \n\n* නැන්දා/මාමා අසනීප වූ විට කටයුතු කරන්නේ කෙසේද?\
                                 \n\n* දෙමව්පියන්ගේ සෞඛ්‍ය තත්ත්වයන් පිලිබඳව සැලකිලිමත්ද?\
                                 \n\n* දරුවන්ගේ අධ්‍යාපන කටයුතු නිසියාකාරව සිදුවේද?")

            elif hymeneal == 2:
                messagebox._show(welcome, \
                                 "* රැකියා ස්ථානයේ ඇතිවන ගැටලු වලට සාර්ථක පිලියම් යෙදිය හැකිද?\
                                 \n\n* පෙම්වතා සම්බන්ධව ගැටලු පවතීද?\
                                 \n\n* තම පෙනුම ගැන සැලකිලිමත් වීමට කාලයක් ඉතිරිද?\
                                 \n\n* පෙම්වතා කොතරම් දුරට සාර්ථකද?\
                                 \n\n* දැන්වත් විවාහයක් සිදුකරගැනීමට අදහසක් පවතීද?\
                                 \n\n* දෙමව්පියන්ගේ සෞඛ්‍ය තත්ත්වයන් පිලිබඳව සැලකිලිමත්ද?\
                                 \n\n* ඔබගේ මිතුරියන් මේවනවිට ගතකරන ජීවිතය කෙබඳුද?")

#-------Application_Interface----------

lblttli=Label(home, text="☻")
lblttli.grid(row=0, column=0, sticky=W+E)
lblttli.config(bg='#909090', fg='#101010', font=('Chiller',32))

lblttl=Label(home, text=("Life Solutions Software"+' '*27))
lblttl.grid(row=0, column=1, columnspan=6, sticky=W)
lblttl.config(bg='#909090', fg='#101010', font=('Chiller',32))

lblfilthsi=Label(home, text="►")
lblfilthsi.grid(row=1, column=0, pady=10, sticky=N+E)
lblfilthsi.config(bg='#C0C0C0', fg='#080808', font=('simsun',17))

lblfilths=Label(home, text="Fill this application correctly,")
lblfilths.grid(row=1, column=1, pady=10, sticky=N+W, columnspan=3)
lblfilths.config(bg='#C0C0C0', fg='#080808', font=('simsun',17))

lblfn=Label(home, text="▪ First name")
lblfn.grid(row=2, column=1, sticky=W)
lblfn.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))
lblco1=Label(home, text=":")
lblco1.grid(row=2, column=2, sticky=W)
lblco1.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))
entfn=ttk.Entry(home, width=45)
entfn.grid(row=2, column=3, columnspan=3, sticky=W)

lblln=Label(home, text="▪ Last name")
lblln.grid(row=3, column=1, sticky=W)
lblln.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))
lblco1=Label(home, text=":")
lblco1.grid(row=3, column=2, sticky=W)
lblco1.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))
entln=ttk.Entry(home, width=45)
entln.grid(row=3, column=3, columnspan=3, sticky=W)

lblgn=Label(home, text="▪ Gender")
lblgn.grid(row=4, column=1, sticky=W)
lblgn.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))
lblco1=Label(home, text=":")
lblco1.grid(row=4, column=2, sticky=W)
lblco1.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))
gend=StringVar()
gend.set(0)
radmale=Radiobutton(home, text="Male", value="1", variable=gend)
radmale.grid(row=4, column=3, sticky=W)
radmale.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))
radfemale=Radiobutton(home, text="Female", value="2", variable=gend)
radfemale.grid(row=4, column=4, sticky=W)
radfemale.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))

dys=[]
yrs=[]
mns=['January','February','March','April','May','June','July','Augast'\
     ,'September','October','November','December']
for i in range(1,32):
       dys.append(i)
for i in range((int(time.localtime()[0])-40),((int(time.localtime()[0]))-15)):
       yrs.append(i)
lblbt=Label(home, text="▪ Birthday")
lblbt.grid(row=5, column=1, sticky=W)
lblbt.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))
lblco1=Label(home, text=":")
lblco1.grid(row=5, column=2, sticky=W)
lblco1.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))
cmbdy=ttk.Combobox(home, values=dys, width=2, state="readonly")
cmbdy.grid(row=5, column=3)
cmbmn=ttk.Combobox(home, values=mns, width=10, state="readonly")
cmbmn.grid(row=5, column=4, sticky=W)
cmbyr=ttk.Combobox(home, values=yrs, width=4, state="readonly")
cmbyr.grid(row=5, column=5, sticky=W)

lblmr=Label(home, text="▪ Marital status")
lblmr.grid(row=6, column=1, sticky=W)
lblmr.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))
lblco1=Label(home, text=":")
lblco1.grid(row=6, column=2, sticky=W)
lblco1.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))
marry=StringVar()
marry.set(0)
radmarr=Radiobutton(home, text="Married", value="1", variable=marry)
radmarr.grid(row=6, column=3, sticky=W)
radmarr.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))
radunmarr=Radiobutton(home, text="Unmarried", value="2", variable=marry)
radunmarr.grid(row=6, column=4, sticky=W)
radunmarr.config(bg='#C0C0C0', fg='#080808', font=('calibri',15))

btngen=Button(home, text="Genarate Problems", command=gen, width=22)
btngen.grid(row=7, column=1, columnspan=4, rowspan=2, pady=10, sticky=S)
btngen.config(bg='#909090', fg='#080808', font=('pristina',21))

lblby=Label(home, text="©")
lblby.grid(row=8, column=5, sticky=E+S)
lblby.config(bg='#C0C0C0', fg='#080808', font=('calibri',10))
lblshn=Label(home, text="Shanuwa")
lblshn.grid(row=8, column=6, sticky=W+S)
lblshn.config(bg='#C0C0C0', fg='#080808', font=('calibri',10))

#-----------------------------------

home.mainloop()
