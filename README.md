<<<<API>>>>

User Authentication and Registration
    /api/v1/token/ - Obtain JWT token for authentication.
    /api/v1/register/ - User registration.


Players
    /api/v1/players/ - List of players (admin only).
    /api/v1/players/<int:pk>/ - Player details (admin only).


Tournaments
    /api/v1/tournaments/ - List, create, update, delete tournaments (admin only).
    /api/v1/tournaments/<int:pk>/ - Tournament details, update, delete (admin only).
    /api/v1/tournaments/<int:pk>/leaderboard/ - Leaderboard for a tournament (all users).

Matches
    /api/v1/matches/ - List, create matches (admin only).
    /api/v1/matches/<int:pk>/ - Match details, update, delete (admin only).

<<<<ISHLATISH>>>>

Foydalanuvchi Ro'yxatdan O'tkazish va Kirish
    Ro'yxatdan o'tish: /api/v1/register/

    POST so'rovi bilan yangi foydalanuvchi ro'yxatdan o'tkazadi. JSON formatida foydalanuvchi ma'lumotlarini yuboring: username, email, va password.
    Kirish: /api/v1/token/

    POST so'rovi bilan JWT token olish uchun foydalanuvchi ma'lumotlarini yuboring: username va password.

<O'yinchilar>
    O'yinchi ro'yxati: /api/v1/players/

    GET so'rovi bilan barcha o'yinchilarni olish (faqat administratorlar uchun).
    POST so'rovi bilan yangi o'yinchi qo'shish (faqat administratorlar uchun). JSON formatida name, age, rating, va country ma'lumotlarini yuboring.

O'yinchi ma'lumotlari: /api/v1/players/<int:pk>/

    GET so'rovi bilan belgilangan o'yinchi haqida ma'lumotlarni olish (faqat administratorlar uchun).
    PUT/PATCH so'rovi bilan belgilangan o'yinchi ma'lumotlarini yangilash (faqat administratorlar uchun).


<Turnirlar>

    Turnir ro'yxati: /api/v1/tournaments/

    GET so'rovi bilan barcha turnirlarni olish.
    POST so'rovi bilan yangi turnir yaratish. JSON formatida name, start_date, end_date ma'lumotlarini yuboring (faqat administratorlar uchun).

Turnir ma'lumotlari: /api/v1/tournaments/<int:pk>/

    GET so'rovi bilan belgilangan turnir haqida ma'lumotlarni olish.
    PUT/PATCH so'rovi bilan belgilangan turnir ma'lumotlarini yangilash (faqat administratorlar uchun).
   
Yetakchilar Jadvali: /api/v1/tournaments/<int:pk>/leaderboard/
    GET so'rovi bilan belgilangan turnir uchun yetakchilar jadvalini olish.


<Matches>

    Matches ro'yxati: /api/v1/matches/

    GET so'rovi bilan barcha juftliklarni olish.
    POST so'rovi bilan yangi juftlik yaratish. JSON formatida tournament, round_number, player1, player2 ma'lumotlarini yuboring (faqat administratorlar uchun).

Matches ma'lumotlari: /api/v1/matches/<int:pk>/

    GET so'rovi bilan belgilangan juftlik haqida ma'lumotlarni olish.
    PUT/PATCH so'rovi bilan belgilangan juftlik ma'lumotlarini yangilash (faqat administratorlar uchun).
