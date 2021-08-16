from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

from django.db.models import Q

def index(request):
	context = {
		#"leagues": League.objects.all(),
		#"teams": Team.objects.all(),
		#"players": Player.objects.all(),

		# SPORTs ORM I
		# ... todas las ligas de béisbol
		#'leagues': League.objects.filter(sport__contains='Baseball'),

		# ... todas las ligas de mujeresw
		#'leagues': League.objects.filter(name__contains='Womens'),
		
		# ... todas las ligas donde el deporte es cualquier tipo de hockey
		#'leagues': League.objects.filter(name__contains='Hockey'),

		# ... todas las ligas donde el deporte no sea football
		#'leagues': League.objects.exclude(sport='Soccer'),

		# ... todas las ligas que se llaman "conferencias"
		#'leagues': League.objects.filter(name__contains='Conference'),

		# ... todas las ligas de la región atlántica
		'leagues': League.objects.filter(Q(name__contains='International') | Q(name__contains='World')), 

		# ... todos los equipos con sede en Dallas
		#"teams": Team.objects.filter(location='Dallas'),

		# ... todos los equipos nombraron los Raptors
		#"teams": Team.objects.filter(team_name='Raptors'),

		# ... todos los equipos cuya ubicación incluye "Ciudad"
		#"teams": Team.objects.filter(location__contains='City'),

		# ... todos los equipos cuyos nombres comienzan con "T"
		#"teams": Team.objects.filter(team_name__startswith='T'),

		# ... todos los equipos, ordenados alfabéticamente por ubicación
		#"teams": Team.objects.all().order_by('location'),

		# ... todos los equipos, ordenados por nombre de equipo en orden alfabético inverso
		#"teams": Team.objects.all().order_by('-team_name'),

		# ... cada jugador con apellido "Cooper"
		#"players": Player.objects.filter(last_name='Cooper'),

		# ... cada jugador con nombre "Joshua"
		#"players": Player.objects.filter(first_name='Joshua'),

		# ... todos los jugadores con el apellido "Cooper" EXCEPTO aquellos con "Joshua" como primer nombre
		#"players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua'),

		# ... todos los jugadores con nombre "Alexander" O nombre "Wyatt"
		#"players": Player.objects.filter(Q(first_name='Alexander') | Q(first_name='Wyatt')),

		# SPORTs ORM II	
		# ... todos los equipos en la Atlantic Soccer Conference
		#"teams": Team.objects.filter(league='5'), # 5 = 'International Amateur Soccer Association'
		"teams": Team.objects.filter(league=League.objects.filter(name='International Amateur Soccer Association').first().id),

		# ... todos los jugadores (actuales) en los Boston Penguins
		#"players": Player.objects.filter(curr_team='9'),
		#"players": Player.objects.filter(curr_team=Team.objects.filter(team_name='Broncos').first().id),

		# ... todos los jugadores (actuales) en la International Collegiate Baseball Conference
		#"players": Player.objects.filter(curr_team=Team.objects.filter(league=League.objects.filter(name='Transamerican Collegiate Basketball Association').first().id).first().id),
		
		# ... todos los jugadores (actuales) en la Conferencia Americana de Fútbol Amateur con el apellido "López"
		
		# ... todos los jugadores de fútbol
		#"players": Player.objects.filter(curr_team=Team.objects.filter(league=League.objects.filter(Q(name__contains='Football') | Q(name__contains='Soccer'))))
		
		# ... todos los equipos con un jugador (actual) llamado "Sophia"
		
		# ... todas las ligas con un jugador (actual) llamado "Sophia"
		
		# ... todos con el apellido "Flores" que NO (actualmente) juegan para los Washington Roughriders
		
		# ... todos los equipos, pasados y presentes, con los que Samuel Evans ha jugado
		
		# ... todos los jugadores, pasados y presentes, con los gatos tigre de Manitoba
		
		# ... todos los jugadores que anteriormente estaban (pero que no lo están) con los Wichita Vikings
		
		# ... cada equipo para el que Jacob Gray jugó antes de unirse a los Oregon Colts
		
		# ... todos llamados "Joshua" que alguna vez han jugado en la Federación Atlántica de Jugadores de Béisbol Amateur
		
		# ... todos los equipos que han tenido 12 o más jugadores, pasados y presentes. (SUGERENCIA: busque la función de anotación de Django).
		
		# ... todos los jugadores y el número de equipos para los que jugó, ordenados por la cantidad de equipos para los que han jugado

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")