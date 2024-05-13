from datetime import datetime

import init_django_orm  # noqa: F401

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
):
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date=None):
    if session_date:
        try:
            return MovieSession.objects.filter(show_time__date=session_date)
        except MovieSession.DoesNotExist:
            return MovieSession.objects.none()
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    update_object = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        update_object.show_time = show_time
    if movie_id is not None:
        update_object.movie_id = movie_id
    if cinema_hall_id is not None:
        update_object.cinema_hall_id = cinema_hall_id
    update_object.save()


def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.get(id=session_id).delete()