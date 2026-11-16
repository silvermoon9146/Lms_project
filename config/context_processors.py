def site_defaults(request):
    return {
        "site_name": "دوره آموزشی دانشکار",
        "site_description": "وبسایت آکوزشی جنگو",
        "is_instructor": request.user.is_authenticated
        and request.user.profile.role == "instructor",
    }
