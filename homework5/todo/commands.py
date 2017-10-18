# -*- coding: utf-8 -*-

from todo.custom_exceptions import UserExitException
from todo.models import BaseItem
from todo.reflection import find_classes


class BaseCommand(object):
    @property
    def label(self) -> str:
        raise NotImplemented()

    def perform(self, store):
        raise NotImplemented()


class ListCommand(BaseCommand):
    @property
    def label(self) -> str:
        return 'list'

    def perform(self, store):
        if len(store.items) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(store.items):
            print('{}: {}'.format(index, str(obj)))


class NewCommand(BaseCommand):
    @property
    def label(self) -> str:
        return 'new'

    @staticmethod
    def _load_item_classes() -> dict:
        # Dynamic load:
        classes = find_classes(BaseItem)
        return dict(classes)

    def perform(self, store):
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{}: {}'.format(index, name))

        selection = None
        selected_key = None

        while True:
            try:
                selection = int(input('Input number: '))
                selected_key = list(classes.keys())[selection]

                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')

        selected_class = classes[selected_key]
        print('Selected: {}'.format(selected_class.__name__))
        print()

        new_object = selected_class.construct()

        store.items.append(new_object)
        print('Added {}'.format(str(new_object)))
        print()
        return new_object


class ExitCommand(BaseCommand):
    @property
    def label(self) -> str:
        return 'exit'

    def perform(self, _store):
        raise UserExitException('See you next time!')

class DoneCommand(BaseCommand):
    @property
    def label(self) -> str:
        return 'done'

    def perform(self, store):

        if len(store.items) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(store.items):
            print('{}: {}'.format(index, str(obj)))

        selection = None

        while True:
            try:
                selection = int(input('Input number: '))
                selection_item = store.items[selection]

                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')

        selection_item.done = True

        print('{}'.format(str(selection_item)))


class UndoneCommand(BaseCommand):
    @property
    def label(self) -> str:
        return 'undone'

    def perform(self, store):

        if len(store.items) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(store.items):
            print('{}: {}'.format(index, str(obj)))

        selection = None

        while True:
            try:
                selection = int(input('Input number: '))
                selection_item = store.items[selection]

                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')

        selection_item.done = False

        print('{}'.format(str(selection_item)))
