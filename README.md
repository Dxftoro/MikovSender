# Что это?
Как сказано в описании данного репозитория - это простая как валенок программа для автоматической отправки отсчётов по лабораторным работам Александру Ивановичу Микову, при этом остаётся возможность переделать код под требования другого преподавателя. Основное назначение этой программы - избавиться от лишней рутины, когда приходится открывать приложение электронной почты, искать шаблон или ранее отправленные письма, копировать их содержимое и подгонять под новую работу - за вас это сделает всемогущий код. Программа написана на Python 3.11, и её реализация вышла настолько простой, что её мог бы написать даже школьник, выучивший Python для сдачи ЕГЭ. Но раз уж я её сделал, и она работает, то почему бы не поделиться этим с нуждающимися?

# Как оно работает?
Программа автоматически берёт информацию из своей концигурации и предоставленного пользователем файла с отсчётом, логинится в указанную почту, составляет письмо с отсчётом и отправляет преподавателю. От пользователя требуется лишь указать путь к файлу с отсчётом либо перетащить его в окно консоли, а затем нажать ENTER.

# Инструкция
## Первичная настройка
1. Откройте файл config.json. Этот файл содержит все самые необходимые для работы программы параметры.
2. В поле с названием "sender" укажите адрес электронной почты, от лица которого будут отправляться ваши отсчёты. Поле receiver можете не менять, если ваш преподаватель - Александр Миков.
3. В поле "app_password" укажите пароль вашей электронной почты. Это нужно, чтобы авторизоваться в вашем аккаунте через эту программу. **Если сервис электронных писем требует для авторизации двухфакторную аутентификацию (например Gmail или Mail.ru), то вместо пароля от электронной почты укажите пароль приложения, предоставляемый используемым вами сервисом**. Если вы используете гугловскую почту (Gmail), то сгенерировать пароль приложения можно [здесь](https://myaccount.google.com/apppasswords).
4. В поле "host" укажите IP хоста, предоставляющего услуги отправки электронных писем. Например, для Gmail - это smtp.gmail.com, для Mail.ru -  smtp.mail.ru.
5. Поле "port" можно не трогать, если программа будет работать исправно. Дело в том, что это порт SMTP-сервера, через который отправляются письма. Обычно порты таких серверов - это 25, 587 и 465. В случае ошибок, вызванных неправильным портом, попробуйте одно из этих значений.
6. В поле "group" укажите группу, в которой вы учитесь.
7. Поле "subgroup" - это ваша подгруппа. Если ваша группа не разделена на подгруппы, оставьте значение 0, если у вас есть подгруппа, то укажите её номер.
8. Поле "description" это поле с текстом, который будет прикреплён к сообщению по мимо файла с отсчётом. Изменять на ваше усмотрение.

## Использование
1. **УБЕДИТЕСЬ, ЧТО ИМЯ ФАЙЛА С ОТСЧЁТОМ СООТВЕТСТВУЕТ СЛЕДУЮЩЕМУ ШАБЛОНУ:**
   ``` Имя Фамилия_лабНомер.docx ```.
  *Пример:* ```Иванов Иван_лаб1.docx```.
   Программа считывает имя и фамилию до символа нижнего подчёркивания и номер работы возле точки!
2. Запустите программу через файл **"launch.bat"**.
3. Введите путь к файлу с отсчётом либо перетащите сам файл в окно программы, тогда путь к нему вставится автоматически.
4. Нажмите ENTER и дождитесь отправки сообщения.
5. Готово, отсчёт должен быть отправлен. Если сомневаетесь, то зайдите в раздел с отправленными сообщениями в вашем электронном почтовом ящике и проверьте, есть ли там что-то новое.

### Любые предложения по изменению и модификации программы приветствуются!
