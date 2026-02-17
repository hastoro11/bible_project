from django.core.management.base import BaseCommand
from bible.models import Book, Verse


class Command(BaseCommand):
    help = 'Load sample Bible data for testing'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample Bible data...')

        # Create Genesis
        genesis, created = Book.objects.get_or_create(
            name='Genesis',
            defaults={
                'abbreviation': 'Gen',
                'testament': 'OT',
                'order': 1,
                'chapter_count': 50
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created book: {genesis.name}'))

        # Add some verses from Genesis 1
        sample_verses = [
            (1, 1, "In the beginning God created the heavens and the earth."),
            (1, 2, "Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters."),
            (1, 3, "And God said, 'Let there be light,' and there was light."),
            (1, 4, "God saw that the light was good, and he separated the light from the darkness."),
            (1, 5, "God called the light 'day,' and the darkness he called 'night.' And there was evening, and there was morning—the first day."),
        ]

        for chapter, verse_num, text in sample_verses:
            verse, created = Verse.objects.get_or_create(
                book=genesis,
                chapter=chapter,
                verse_number=verse_num,
                defaults={'text': text}
            )
            if created:
                self.stdout.write(f'  Added verse: Genesis {chapter}:{verse_num}')

        # Create John (Gospel)
        john, created = Book.objects.get_or_create(
            name='John',
            defaults={
                'abbreviation': 'Jn',
                'testament': 'NT',
                'order': 43,
                'chapter_count': 21
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created book: {john.name}'))

        # Add some verses from John 3
        john_verses = [
            (3, 16, "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life."),
            (3, 17, "For God did not send his Son into the world to condemn the world, but to save the world through him."),
            (3, 18, "Whoever believes in him is not condemned, but whoever does not believe stands condemned already because they have not believed in the name of God's one and only Son."),
        ]

        for chapter, verse_num, text in john_verses:
            verse, created = Verse.objects.get_or_create(
                book=john,
                chapter=chapter,
                verse_number=verse_num,
                defaults={'text': text}
            )
            if created:
                self.stdout.write(f'  Added verse: John {chapter}:{verse_num}')

        # Create Psalms
        psalms, created = Book.objects.get_or_create(
            name='Psalms',
            defaults={
                'abbreviation': 'Ps',
                'testament': 'OT',
                'order': 19,
                'chapter_count': 150
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created book: {psalms.name}'))

        # Add Psalm 23
        psalm_verses = [
            (23, 1, "The LORD is my shepherd, I lack nothing."),
            (23, 2, "He makes me lie down in green pastures, he leads me beside quiet waters,"),
            (23, 3, "he refreshes my soul. He guides me along the right paths for his name's sake."),
            (23, 4, "Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me."),
            (23, 5, "You prepare a table before me in the presence of my enemies. You anoint my head with oil; my cup overflows."),
            (23, 6, "Surely your goodness and love will follow me all the days of my life, and I will dwell in the house of the LORD forever."),
        ]

        for chapter, verse_num, text in psalm_verses:
            verse, created = Verse.objects.get_or_create(
                book=psalms,
                chapter=chapter,
                verse_number=verse_num,
                defaults={'text': text}
            )
            if created:
                self.stdout.write(f'  Added verse: Psalms {chapter}:{verse_num}')

        self.stdout.write(self.style.SUCCESS('\nSample data loaded successfully!'))
        self.stdout.write('Books created: Genesis, John, Psalms')
        self.stdout.write(f'Total verses: {Verse.objects.count()}')
