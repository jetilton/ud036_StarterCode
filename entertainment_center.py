# -*- coding: utf-8 -*-
from media import Movie


nice_guys = Movie('The Nice Guys', 
                  'http://img.moviepostershop.com/' \
                  'the-nice-guys-movie-poster-2016-1020773127.jpg', 
                  'https://www.youtube.com/watch?v=Ihb8vCrj2kc')
django = Movie('Django',
               'https://imgc.allpostersimages.com/img/posters/' \
               'django-unchained_u-L-F5UPZN0.jpg?src=gp&w=300&h=375',
               'https://www.youtube.com/watch?v=eUdM9vrCbow')
shawshank = Movie('Shawshank Redemption', 
                  'https://images-na.ssl-images-amazon.com/' \
                  'images/I/51B1ehfX4pL.jpg', 
                  'https://www.youtube.com/watch?v=6hB3S9bIaco')

movie_list = [nice_guys, django, shawshank]