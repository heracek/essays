from django.db import models
from utils import split_text_to_words_dict_with_counts
from StringIO import StringIO

class Essay(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    text = models.TextField(blank=True)

    def __unicode__(self):
        return u'Essay: %s' % self.title
    
    def save(self):
        super(Essay, self).save()
        
        for hyperwordinessay in self.hyperwordsinessays_set.select_related(depth=1).all():
            hyperwordinessay.hyperword.count -= hyperwordinessay.count
            hyperwordinessay.hyperword.save()
            
            hyperwordinessay.delete()
        
        for (word, count) in split_text_to_words_dict_with_counts(self.text).iteritems():
            try:
                hyperword = HyperWord.objects.get(word=word)
                hyperword.count += count
                hyperword.save()
                
            except HyperWord.DoesNotExist:
                hyperword = HyperWord.objects.create(word=word, count=count)
            
            HyperWordsInEssays.objects.create(hyperword=hyperword, essay=self, count=count)
    
    def get_hypertexted_text(self):
        hypertexted_text = StringIO()
        last_aplha_chars_len = 0
        
        def get_hypertexted_word(word):
            try:
                hyperword = HyperWord.objects.get(word=word.lower())
                return '<a href="%s" class="word-%s">%s</a>' % (hyperword.get_absolute_url(), hyperword.word, word)
            except HyperWord.DoesNotExist:
                return word
                
        
        for (i, char) in enumerate(self.text):
            if char.isalpha():
                last_aplha_chars_len += 1
            else:
                if last_aplha_chars_len:
                    word = self.text[i-last_aplha_chars_len:i]
                    
                    hypertexted_text.write(get_hypertexted_word(word))
                    
                    last_aplha_chars_len = 0
                hypertexted_text.write(char)
        if last_aplha_chars_len:
            word = self.text[-last_aplha_chars_len:]
            hypertexted_text.write(get_hypertexted_word(word))
        
        hypertexted_text.seek(0)
        return hypertexted_text.read()
    get_hypertexted_text.allow_tags = True
    get_hypertexted_text.short_description = 'Hypertexted text'
        

class HyperWord(models.Model):
    word = models.SlugField()
    essays = models.ManyToManyField(Essay, through='HyperWordsInEssays')
    count = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'HyperWord: %s' % self.word
    
    def get_absolute_url(self):
        return '/word/%s/' % self.word
    
class HyperWordsInEssays(models.Model):
    hyperword = models.ForeignKey(HyperWord)
    essay = models.ForeignKey(Essay)
    count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-count']
