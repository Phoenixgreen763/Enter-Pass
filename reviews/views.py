from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Associate the review with the logged-in user
            review.save()
            return redirect('review_list')  # Redirect to the review list page
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review has been deleted successfully!')
        return redirect('review_list')  # Adjust this URL to wherever you list reviews

    return render(request, 'reviews/delete_review.html', {'review': review})