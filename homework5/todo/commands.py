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
