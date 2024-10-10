from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Associate the review with the logged-in user
            review.save()
            return redirect('review_list')  # Redirect to the reviews page after submitting

    context = {
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'reviews/review_list.html', context)
