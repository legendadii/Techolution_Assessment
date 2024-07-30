from django.shortcuts import render, get_object_or_404, redirect


def library_management(request):
    return render(request, 'base.html')