from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    This function will simply render the home page of the site.
    """
    return render(request, 'index.html')


def analyze(request):
    """
        This function will do the manipulation with the text and    
        return the analyzed text.
    """

    # accessing the text from the textbox.
    djtext = request.POST.get('text', 'default')
    # remove punctuation button.
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')  # Upper case button.
    # New line remover button.
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount', 'off')  # charatcer count button.
    # Extra space remover button.
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc == "on":
        # if the punctuation button will be on ,then it will remove the punctuations form the text.
        Punctuations = '''!?()-[]{}:;'"\\<>/?@#$%^&*_.~'''
        analyzed = ""
        for char in djtext:
            if char not in Punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removing Punctuations',
                  'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        # if uppercase button is on, then it will convet all the characters of the text into UPPER case.
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        # if the remove new line button will be on, then it will remove the new lines from the text.
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        # if the remove extra space button is on, then it will remove the extra spaces from the text.
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        # is the character count button is on then it will count the number of characters in the text.
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'purpose': 'Character count',
                  'analyzed_text': ['Total Characters-', analyzed]}

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        # this is used to show the errors.
        return HttpResponse("Error.")

    return render(request, 'analyze.html', params)
