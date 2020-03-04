<template>
    <ContentBox>
        <div>
            <span>{{msg}}</span>
        </div>
    </ContentBox>
</template>
<script>
import ContentBox from '@/components/ContentBox'
export default {
    components:{
        ContentBox
    },
    data(){
        return{
            msg: 'Publication'
        }
    }
};
</script>