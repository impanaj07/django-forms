from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .forms import ReviewForm

# Create your views here.
def review(request):
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            review_text = form.cleaned_data['review']
            entered_text = f"Name: {user_name}, Review: {review_text}"

        print(entered_text)
        return HttpResponseRedirect('/thank_you/')
    form=ReviewForm()
    return render(request,"reviews/review.html", {'form': form} )
def thank_you(request):
    return render(request,"reviews/thank_you.html")