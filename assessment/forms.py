from django import forms

# Depression Assessment Form
class DepressionTest(forms.Form):
    CHOICES = [(0, ''), (1, ''),
               (2, ''), (3, '')]

    phq_1 = forms.ChoiceField(
        label='I feel overwhelmingly sad at times',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    phq_2 = forms.ChoiceField(
        label='When I think of the future I feel hopeless',
        choices=CHOICES, 
        widget=forms.RadioSelect(attrs={'class':''}))

    phq_3 = forms.ChoiceField(
        label='I feel like a complete failure',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_4 = forms.ChoiceField(
        label='I feel guilty about something most of the time',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_5 = forms.ChoiceField(
        label='I feel like I am being punished',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_6 = forms.ChoiceField(
        label='I feel disappointed (even disgusted) with myself',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_7 = forms.ChoiceField(
        label='I am often on the brink of tears or just want to cry',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_8 = forms.ChoiceField(
        label='I am so tired I don’t have the energy to do anything',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    phq_9 = forms.ChoiceField(
        label='My sleep patterns have been really disrupted',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_10 = forms.ChoiceField(
        label='I find it really hard to do anything, especially work',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

# Anxiety Assessment Form
class AnxietyTest(forms.Form):
    CHOICES = [(0, ''), (1, ''),
               (2, ''), (3, '')]

    phq_1 = forms.ChoiceField(
        label='I find it very hard to unwind, relax or sit still',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    phq_2 = forms.ChoiceField(
        label='I have had stomach problems, such as feeling sick or stomach cramps',
        choices=CHOICES, 
        widget=forms.RadioSelect(attrs={'class':''}))

    phq_3 = forms.ChoiceField(
        label='I have been irritable and easily become annoyed',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_4 = forms.ChoiceField(
        label='I have experienced shortness of breath',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_5 = forms.ChoiceField(
        label='I have felt dizzy and unsteady at times',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_6 = forms.ChoiceField(
        label='I have had difficulties with sleep (including waking early, finding it hard to go to sleep)',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_7 = forms.ChoiceField(
        label='I have felt panicked and overwhelmed by things in my life',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_8 = forms.ChoiceField(
        label='I have felt nervous and on edge',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    phq_9 = forms.ChoiceField(
        label='I have had trembling hands',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_10 = forms.ChoiceField(
        label='I seem to be constantly worrying about things',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

# Stress Assessment Form
class StressTest(forms.Form):
    CHOICES = [(0, ''), (1, ''),
               (2, ''), (3, '')]

    phq_1 = forms.ChoiceField(
        label='I have found myself getting upset by quite trivial things',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    phq_2 = forms.ChoiceField(
        label='I have experienced breathing difficulties',
        choices=CHOICES, 
        widget=forms.RadioSelect(attrs={'class':''}))

    phq_3 = forms.ChoiceField(
        label='I tend to overreact to situations',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_4 = forms.ChoiceField(
        label='I have felt shakey like my legs are going to give way',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_5 = forms.ChoiceField(
        label='I have found myself getting upset easily',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_6 = forms.ChoiceField(
        label='I have found myself getting impatient when I have been delayed in any way',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_7 = forms.ChoiceField(
        label='I have experienced sweaty palms or perspiration for no physical reasons',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_8 = forms.ChoiceField(
        label='I have felt scared or nervous for no good reason',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    phq_9 = forms.ChoiceField(
        label='I have had a sense of nervous tension, like being on edge all the time',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_10 = forms.ChoiceField(
        label='It has been difficult for me to tolerate interruptions to what I was doing',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))