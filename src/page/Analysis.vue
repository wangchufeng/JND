<template>
    <ContentBox>
        <v-row class="text-center">
            <v-col cols="12">
                <!-- <v-img
              :src="require('../assets/logo.svg')"
              class="my-3"
              contain
              height="100"
            /> -->
            </v-col>

            <v-col class="mb-1">
                <h1 class="display-2 font-weight-bold mb-3">
                    Result Analysis
                </h1>
                <p class="subheading font-weight-regular">
                    Enter the test ID and return the result analysis
                </p>
            </v-col>

            <v-col class="mb-1" cols="12">
                <v-row justify="center">
                    <v-col class="mb-1" cols="2">
                        <v-text-field label="Input ID" v-model="inputId" hide-details="auto">
                        </v-text-field>
                        <v-btn :disabled="!valid" color="success" class="mr-4 mt-2" @click="validate">
                            Analysis
                        </v-btn>
                    </v-col>
                </v-row>

                <v-row justify="center">

                </v-row>
            </v-col>

            <v-col class="mb-5" cols="12">
                <h2 class="headline font-weight-bold mb-3">
                    Experiment Result
                </h2>

                <v-row justify="center">
                    <v-simple-table>
                        <template v-slot:default>
                            <thead>
                                <tr>
                                    <th class="text-left .display-4">Name</th>
                                    <th class="text-left .display-4">Result</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item in resultTable" :key="item.name">
                                    <td>{{ item.name }}</td>
                                    <td>{{ item.result }}</td>
                                </tr>
                            </tbody>
                        </template>
                    </v-simple-table>
                </v-row>
            </v-col>
        </v-row>
    </ContentBox>
</template>
<script>
    import ContentBox from '@/components/ContentBox'

    export default {
        components: {
            ContentBox
        },
        mounted() {
            var params = new URLSearchParams();
            params.append('id', this.inputId);
            this.$axios({
                    method: 'post',
                    url: '/server/getNewData',
                    data: params
                }).then(function (response) {
                    console.log(response);
                })
                .catch(function (error) {
                    console.log(error);
                });
        },
        computed: {
            valid() {
                if (this.inputId % 1 == 0 && this.inputId !== '' && this.inputId !== null) {
                    return true
                } else {
                    return false
                }
            }
        },
        data() {
            return {
                inputId: null,
                msg: 'Analysis',
                resultTable: []
            }
        },
        methods: {
            validate() {
                var params = new URLSearchParams();
                params.append('id', this.inputId);
                this.$axios({
                        method: 'post',
                        url: '/server/info',
                        data: params
                    }).then((response) => {
                        var user_id = {
                            'name': 'id',
                            'result': this.inputId
                        }
                        var accuracy = {
                            'name': 'accuracy',
                            'result': response.data.accuracy
                        }
                        var total_test_num = {
                            'name': 'total_test_num',
                            'result': response.data.total_test_num
                        }
                        var test_type = {
                            'name': 'test_type',
                            'result': response.data.test_type
                        }
                        this.resultTable = []
                        this.resultTable.push(user_id,accuracy, total_test_num, test_type)
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
                return 0
            }
        }
    };
</script>
<style>


</style>