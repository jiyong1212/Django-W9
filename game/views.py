from django.shortcuts import render, redirect
from random import *
from .models import Weapon, Character
from .forms import WeaponForm, CharacterForm

# Create your views here.
win = 0
draw = 0
lose = 0

def game_list(request):
    return render(request, 'game/game_list.html')

def rsp_select(request):
    global win, draw, lose
    context = {
        'win': win,
        'draw': draw,
        'lose': lose,
    }
    return render(request, 'game/rsp_select.html', context)

def rsp_result(request, pick):
    global win, draw, lose
    rsp = ['가위', '바위', '보']
    com = choice(rsp)

    if pick == com:
        result = '무승부'
        draw += 1
    elif (pick == '가위' and com == '보') or (pick == '바위' and com == '가위') or (pick == '보' and com == '바위'):
        result = '승리'
        win += 1
    else :
        result = '패배'
        lose += 1

    context = {
        'pick': pick,
        'com': com,
        'result': result,
        'win': win,
        'draw': draw,
        'lose': lose,
    }
    return render(request, 'game/rsp_result.html', context)

def rsp_reset(request):
    global win, draw, lose
    win, draw, lose = 0, 0, 0
    return redirect('game:rsp_select')

def weapon_create(request):
    if request.method == 'POST':
        weapon_form = WeaponForm(request.POST)
        
        if weapon_form.is_valid():
            weapon_form.save()
            return redirect('game:weapon_list')
    else:
        weapon_form = WeaponForm()
    
    context = {
        'weapon_form': weapon_form,
    }
    return render(request, 'game/weapon_form.html', context)

def weapon_list(request):
    weapons = Weapon.objects.all()

    default_weapons = {
        '주먹도끼': 1,
        '수상한 막대기': 7,
        '낡은 검': 5,
        '가벼운 물총': 3,
        '수학의 정석': 9,
    }
    
    if len(weapons) == 0:
        for weapon in default_weapons:
            Weapon.objects.create(
                name = weapon,
                power = default_weapons[weapon],
            )
        weapons = Weapon.objects.all()

    context = {
        'weapons': weapons,
    }
    return render(request, 'game/weapon_list.html', context)

# 게임은 하나의 캐릭터로 진행
def adventure_home(request):
    # 캐릭터 객체가 하나도 없는 경우
    if Character.objects.all().count() == 0:
        if request.method == 'POST':
            # Character의 weapon 필드에는 비어있는 객체가 저장될 수 있으므로 임시저장할 필요가 없음
            character_form = CharacterForm(request.POST)
            character_form.save()
            return redirect('game:adventure_home')
        else:
            character_form = CharacterForm()
        context = {
            'character_form': character_form,
        }
        return render(request, 'game/character_create.html', context)
    
    # 캐릭터가 생성된 경우
    else:
        # [코드 수정] Character 모델 중 id가 1인 캐릭터 객체를 가져옴
        # [코드 수정] None을 지우고 작성
        character = Character.objecter.objects.get(id=1)
        context = {
            'character': character,
        }
        # [코드 수정] character의 weapon 필드에 아무것도 저장되어 있지 않은 경우
        # [코드 수정] None을 지우고 작성
        if character.weapon == None:
            # [코드 수정] 'game/adventure_new.html'로 이동하도록 코드 작성
            # [코드 수정] None을 지우고 작성
            return render(request,'game/adventure_new.html' , context)
    return render(request, 'game/adventure_home.html', context)

# 캐릭터에게 랜덤으로 무기 장착
def weapon_get(request):
    # [코드 수정] Character 모델 중 id가 1인 캐릭터 객체를 가져옴
    # [코드 수정] None을 지우고 작성
    character = Character.objecter.objects.get(id=1)
    
    weapons = Weapon.objects.all()
    # [코드 수정] random 모듈의 choice 함수를 이용하여 selected_weapon 변수에 저장
    # [코드 수정] None을 지우고 작성
    selected_weapon = choice(weapons)
    
    character.weapon = selected_weapon
    character.save()

    context = {
        'character': character,
    }
    return render(request, 'game/adventure_home.html', context)
