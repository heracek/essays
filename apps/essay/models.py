from django.db import models
from utils import split_text_to_words_dict_with_counts

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
        

class HyperWord(models.Model):
    word = models.CharField(max_length=100)
    essays = models.ManyToManyField(Essay, through='HyperWordsInEssays')
    count = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'HyperWord: %s' % self.word
    
class HyperWordsInEssays(models.Model):
    hyperword = models.ForeignKey(HyperWord)
    essay = models.ForeignKey(Essay)
    count = models.IntegerField(default=0)
