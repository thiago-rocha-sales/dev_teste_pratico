<template>

    <section>

      <button class="button is-primary is-medium" @click="onCreate">
        Nova Plataforma
      </button>
    
      <b-table :data="data" :bordered="true" :loading="loading">
        <template slot-scope="props">
          <b-table-column field="id" label="ID" width="40" numeric>
            {{ props.row.id }}
          </b-table-column>

          <b-table-column field="nome" label="Plataforma">
            {{ props.row.nome }}
          </b-table-column>

          <b-table-column custom-key="actions" width="100">
            <button class="button is-small is-light" @click="onEdit(props.row)">
              <b-icon icon="pencil" size="is-small"></b-icon>
            </button>
            <button class="button is-small is-danger" @click="onDelete(props.row)">
              <b-icon icon="delete" size="is-small"></b-icon>
            </button>
          </b-table-column>

        </template>
      </b-table>

      <b-modal :active.sync="isComponentModalActive" has-modal-card>
          <modal-form v-bind="formProps"></modal-form>
      </b-modal>
    </section>
</template>

<script>
    import {APIService} from './APIService'
  
    const apiService = new APIService()

    const ModalForm = {
        props: ['nome', 'id'],
        methods: {
          onSave () {
            // console.log(this.data)
            
            if (this.id) {
              const plataforma = {
                id: this.id,
                nome: this.nome
              }
              apiService.updatePlataformas(plataforma).then((data) => {
                console.log(data)
                this.$parent.close()
              })
            } else {
              const plataforma = {
                nome: this.nome
              }
              apiService.createPlataformas(plataforma).then((data) => {
                console.log(data)
                this.$parent.close()
              })
            }
          }
        },
        template: `
            <form @submit="onSave">
                <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                        <p class="modal-card-title">Editar</p>
                    </header>
                    <section class="modal-card-body">
                        <b-field label="Plataforma">
                            <b-input
                                type="text"
                                :value="nome"
                                v-model="nome"
                                placeholder=""
                                required>
                            </b-input>
                        </b-field>

                        <b-field>
                            <b-input
                                type="hidden"
                                :value="id"
                                v-model="id"
                                required>
                            </b-input>
                        </b-field>

                    </section>
                    <footer class="modal-card-foot">
                        <button class="button" type="button" @click="$parent.close()">Fechar</button>
                        <button class="button is-primary">Gravar</button>
                    </footer>
                </div>
            </form>
        `
    }
    
    export default {
        name: 'plataformas',
        components: {
          ModalForm
        },
        data() {
            return {
                isComponentModalActive: false,
                formProps: {
                  nome: '',
                  id: ''
                },
                data: [],
                loading: false
            }
        },
        methods: {
          getPlataformas() {
            this.loading = true
            apiService.getPlataformas().then((data) => {
                  this.data = data.results
                  // console.log(data)
                  this.loading = false
                  // this.searched = this.plataformas
            })
          },
          onDelete (row) {
            // this.loading = true
            apiService.deletePlataformas(row.id).then((data) => {
              // console.log(data)
              this.getPlataformas()
              // this.loading = false
            })
          },
          onEdit (row) {
            // console.log(row)
            this.isComponentModalActive = true
            this.formProps.nome = row.nome
            this.formProps.id = row.id
            // this.$modal.open({
            //   parent: this,
            //   component: ModalForm,
            //   props: {
            //     'nome': row.nome,
            //     'id': row.id
            //   }
            // })
          },
          onPageChange(page) {
            this.page = page
            this.getPlataformas()
          },
          onCreate() {
            this.isComponentModalActive = true
          }
        },
        mounted() {
          this.getPlataformas()
          // console.log('Mounted !')
        },
    }  
</script>