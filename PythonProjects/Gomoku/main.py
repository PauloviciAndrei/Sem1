from ui import UI
from services import Services
from repository import Repository
from domain import Piece
from bot import Bot
from exceptions import Invalid_command
from exceptions import Invalid_Move


def main():
    repository = Repository(Piece)
    bot = Bot()
    services = Services(repository, bot)
    invalid_command = Invalid_command
    invalid_move = Invalid_Move
    ui = UI(services, invalid_command, invalid_move)
    ui.run()


main()
