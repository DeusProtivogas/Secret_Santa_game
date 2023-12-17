import asyncio
from django.contrib import admin
from .models import Game, Patricipants, Givers
# from .forms import UsersForm
from asgiref.sync import async_to_sync
from .gifting import perform_pairing
from secret_santa.bot_logic.handlers.default_handlers.new_game import announce



@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    actions = ["make_published"]
    @admin.action(description="Ручная жеребьевка выбранных игр")
    def make_published(modeladmin, request, queryset):
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)

        # asyncio.run(announce(list(queryset)))
        perform_pairing(list(queryset))

    list_display = ('id', 'name_of_game', 'creators_id', 'cost_of_the_gift',
                    'start_of_registration', 'end_of_registration', 'departure_date',
                    'link_to_the_game'
                    )
    # form = UsersForm


@admin.register(Patricipants)
class PatricipantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'id_user', 'name',
                    'e_mail', 'interests', 'letter_to_santa'
                    )


@admin.register(Givers)
class GiversAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'givers', 'recipient'
                    )
