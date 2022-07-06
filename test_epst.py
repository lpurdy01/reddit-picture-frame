import ep_st

pic_file_types = ['jpg', 'png', 'gif']


def test_fix_imgur():
    assert ep_st.fix_imgur('https://imgur.com/12345') == 'https://i.imgur.com/12345.png'
    assert ep_st.fix_imgur('http://imgur.com/12345') == 'https://i.imgur.com/12345.png'
    assert ep_st.fix_imgur('i.imgur.com') == 'i.imgur.com'
    assert ep_st.fix_imgur('imgtest.com') == 'imgtest.com'

    img = ep_st.fix_imgur('https://imgur.com/gallery/UrW5yWV')
    assert 'i.imgur' in img
    assert img.split('.')[-1] in pic_file_types

    img = ep_st.get_album_image('https://imgur.com/a/UrW5yWV')
    assert 'i.imgur' in img
    assert img.split('.')[-1] in pic_file_types