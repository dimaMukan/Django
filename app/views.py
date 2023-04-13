from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

def name(request):
    return HttpResponse("123")



info_dict = {
    "one":"ONE!",
    "two":"TWO!",
    "three":"THREE!",
    "four":"FOUR!",
    "five":"FIVE!",
}

def hello(request):
    num = list(info_dict)
    li=''
    for i in num:
        redirect_url = reverse('info',args=[i])
        li += f"<li><a href= '{redirect_url}'> {i} </a> </li>"
    res = f"""
    <ol>
        {li}
    </ol>
    """
    return HttpResponse(res)

def get_info(request,info:str):
    description = info_dict.get(info,None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound("NOT FOUND))))))!")

def number(request, num:int):
    numbers = list(info_dict)
    if num > len(numbers):
        return HttpResponseNotFound(f"NOT FOUND! - {num}")
    res = numbers[num - 1]
    a = reverse('info',args=(res,))
    return HttpResponseRedirect(a)
