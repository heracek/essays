from django.db import models

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
